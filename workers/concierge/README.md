# FulcrumGrid concierge Worker (`fg-concierge`)

Cloudflare Worker that backs the concierge voice character on fulcrumgrid.com.
It holds all API keys server-side and exposes two endpoints to the front-end
widget (`assets/js/concierge.js`):

- `POST /chat` — streams the assistant's answer as Server-Sent Events
  (`data: {"delta":"..."}` lines, ending with `data: {"done":true}`).
- `POST /tts` — returns spoken audio as `audio/mpeg`.
- `OPTIONS` on both — CORS preflight.

The Worker is dependency-free: plain `fetch` + Web Streams, no npm packages.

---

## Choose the brain: Anthropic or DeepSeek

`/chat` works with either, chosen by the `LLM_PROVIDER` var — no code change:

- `LLM_PROVIDER = "anthropic"` (default) → set secret `ANTHROPIC_API_KEY`, var `ANTHROPIC_MODEL` (default `claude-haiku-4-5`).
- `LLM_PROVIDER = "deepseek"` → set secret `DEEPSEEK_API_KEY`, vars `DEEPSEEK_MODEL` (default `deepseek-chat`) and `DEEPSEEK_BASE_URL` (default `https://api.deepseek.com`). The DeepSeek path is OpenAI-compatible, so the same setting works for OpenAI/Groq/Together/Mistral by changing the base URL, model, and key.

Either way you still set `ELEVENLABS_API_KEY` for the voice. **Privacy note:** visitor messages go to whichever provider you pick; DeepSeek is a China-based service, so disclose it in the site's consent/privacy copy if you use it.

---

## Deploy with NO local repo (all in the browser)

If you don't have the repo (or wrangler) on a machine, deploy from the Cloudflare dashboard:

1. **dash.cloudflare.com → Workers & Pages → Create → Create Worker.** Name it `fg-concierge`, deploy the starter, then **Edit code**.
2. In the editor, select-all, delete, and paste the full contents of **`workers/concierge/src/index.js`** (copy it from GitHub: open the file → "Copy raw file"). **Deploy.**
3. **KV:** Workers & Pages → **KV → Create namespace** `RL`. Back in the Worker → **Settings → Bindings → Add → KV namespace**, variable name `RL`, pick `RL`.
4. **Settings → Variables & Secrets** — add:
   - Secrets: `ELEVENLABS_API_KEY`, and `ANTHROPIC_API_KEY` *or* `DEEPSEEK_API_KEY` (whichever provider).
   - Text vars: `ALLOWED_ORIGINS` = `https://fulcrumgrid.com`, `LLM_PROVIDER` = `anthropic` (or `deepseek`), `ELEVENLABS_VOICE_ID` = your voice id, plus the model vars you want (`ANTHROPIC_MODEL` / `DEEPSEEK_MODEL`, `ELEVENLABS_MODEL`).
   - **Deploy** again so the bindings take effect.
5. Copy the Worker URL (`https://fg-concierge.<you>.workers.dev`) — that's your **WORKER_ORIGIN**. Send it to whoever flips the site flag (step 6 below), or set it yourself.

The CLI path below does the same thing from a checkout; use whichever you prefer.

---

## 1. Install Wrangler

```bash
npm install -g wrangler        # or: npm i -D wrangler and use `npx wrangler`
wrangler login                 # authenticate with your Cloudflare account
```

Everything below is run from this directory (`workers/concierge/`).

## 2. Create the rate-limit KV namespace

```bash
wrangler kv namespace create RL
```

Copy the printed `id` into `wrangler.toml`, replacing the `<KV_ID>` placeholder:

```toml
[[kv_namespaces]]
binding = "RL"
id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

(If KV is ever unavailable at runtime the Worker fails **open** — requests are
allowed rather than blocked.)

## 3. Set the secrets

These are **never** stored in `wrangler.toml` or git:

```bash
wrangler secret put ANTHROPIC_API_KEY     # your Anthropic key
wrangler secret put ELEVENLABS_API_KEY    # your ElevenLabs key
```

## 4. Set the ElevenLabs voice id

Pick a voice in the ElevenLabs dashboard and put its id in `wrangler.toml`:

```toml
[vars]
ELEVENLABS_VOICE_ID = "your_voice_id_here"
```

Optionally review the other `[vars]`: `ALLOWED_ORIGINS` (CORS allow-list),
`ANTHROPIC_MODEL` (default `claude-haiku-4-5`), and `ELEVENLABS_MODEL`
(default `eleven_multilingual_v2`).

## 5. Deploy

```bash
wrangler deploy
```

Wrangler prints the deployed origin, e.g.
`https://fg-concierge.<your-subdomain>.workers.dev` (or your custom route such
as `https://concierge.fulcrumgrid.com`). This is the **WORKER_ORIGIN**.

You can smoke-test locally first with `wrangler dev` (secrets still come from
`wrangler secret put`, or from a local `.dev.vars` file you do **not** commit).

## 6. Wire the site to the Worker

Edit `scripts/build/concierge_config.py` at the repo root:

```python
WORKER_ORIGIN = 'https://fg-concierge.<your-subdomain>.workers.dev'  # no trailing slash
ENABLED = True
```

Then rebuild the static site (run the project's build, e.g.
`python scripts/build/build.py`) and deploy GitHub Pages as usual. The widget
is only injected once `ENABLED = True` **and** a non-empty `WORKER_ORIGIN` is
set; `WORKER_ORIGIN` is also added to each page's CSP `connect-src`.

Keep `ALLOWED_ORIGINS` in `wrangler.toml` in sync with where the site is served
from (production domain plus `http://localhost:8000` for local preview).

---

## Knowledge source

`knowledge.md` is the **human-editable** factual brief about FulcrumGrid.
The Worker embeds the same text as the `KNOWLEDGE` const near the top of
`src/index.js` (so the Worker stays a single self-contained file — no bundler,
no build step). When facts change (prices, apps, regions):

1. Edit `knowledge.md`.
2. Paste the updated body into the `KNOWLEDGE` template literal in
   `src/index.js`.
3. `wrangler deploy`.

## Swap TTS to Cartesia (or another vendor)

TTS lives in a single, clearly-marked function, `ttsSynthesize(env, text, lang)`
in `src/index.js`. Only that function knows the vendor; `/tts` just calls it and
streams back the returned mp3 bytes. To switch to
[Cartesia](https://docs.cartesia.ai/) (Sonic), replace the function body with a
call to `https://api.cartesia.ai/tts/bytes` using header `X-API-Key` (and
`Cartesia-Version`), a `model_id` such as `sonic-2`, `voice: { mode: "id", id:
<voice> }`, and `output_format` set to MP3. Keep the return shape
`{ ok, status, body }` where `body` is the mp3 byte stream, and add a
`CARTESIA_API_KEY` secret plus a `CARTESIA_VOICE_ID` var. Nothing else in the
Worker changes.

## Cost & rate-limit tuning

Rate limits are constants at the top of `src/index.js`:

- `IP_MAX_REQUESTS` / `IP_WINDOW_SEC` — per-IP sliding window
  (default **30 requests / 10 minutes**, keyed on `cf-connecting-ip`).
- `SESSION_MAX_PER_DAY` — per-`sessionId` cap (default **40 messages / day**).
- `CHAT_MAX_TOKENS` — max tokens per answer (default **400**; lower it to cut
  Anthropic cost, raise it for longer answers).
- `MAX_TTS_CHARS` — text truncated before TTS (default **800**; TTS is usually
  the biggest cost driver, so this directly bounds spend per spoken reply).
- `MAX_MESSAGE_CHARS` (1000) and `MAX_HISTORY_TURNS` (10) bound the prompt size
  sent to Anthropic, which also bounds input-token cost.

Tighten the IP/session limits if you see abuse; loosen them if legitimate users
hit the cap. Because rate limiting fails open, a KV outage will not take chat
down — it only disables throttling until KV recovers.
