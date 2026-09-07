# Google Indexing API

Notify Google to (re)crawl specific URLs, using a service-account credential.

> **Reality check.** Google officially supports the Indexing API only for pages
> with `JobPosting` or `BroadcastEvent` structured data. For ordinary marketing
> pages it often ignores or deprioritizes submissions. Your **sitemap**
> (`/sitemap.xml`) and the **URL Inspection → Request Indexing** button in Search
> Console remain the reliable channels for Google; **IndexNow**
> (`scripts/indexnow-submit.sh`) covers Bing/Yandex. Treat this API as a bonus
> nudge, not the main path.

Everything in code is ready. You only need to do the one-time Google setup below,
then either run the script locally or trigger the GitHub Action.

---

## One-time setup (≈10 minutes, only you can do this)

1. **Create/pick a Google Cloud project** — https://console.cloud.google.com/projectcreate
   (e.g. name it `fulcrumgrid-indexing`).

2. **Enable the Indexing API** for that project —
   https://console.cloud.google.com/apis/library/indexing.googleapis.com → **Enable**.

3. **Create a service account** —
   https://console.cloud.google.com/iam-admin/serviceaccounts → **Create service account**.
   - Name: `indexing-bot` (no roles/permissions needed on this screen — skip them).
   - After creating it, open the account → **Keys** → **Add key** → **Create new key**
     → **JSON**. A `.json` file downloads. Keep it secret.

4. **Grant the service account access in Search Console** — this is the step people miss.
   - Open https://search.google.com/search-console → select the **fulcrumgrid.com** property.
   - **Settings → Users and permissions → Add user**.
   - Paste the service account's email (looks like
     `indexing-bot@your-project.iam.gserviceaccount.com`, found in the JSON as
     `client_email`), and set permission to **Owner** (the API requires Owner).

That's it. Now use either option below.

---

## Option A — GitHub Action (no local tools needed)

1. In the repo: **Settings → Secrets and variables → Actions → New repository secret**.
   - Name: `GOOGLE_INDEXING_SA_KEY`
   - Value: paste the **entire contents** of the service-account JSON file.
2. Go to the repo's **Actions** tab → **Google Indexing API** → **Run workflow**.
   - Leave *URLs* blank to submit everything in [`urls.txt`](./urls.txt), or paste
     space-separated URLs to submit just those.
   - Pick `URL_UPDATED` (new/changed) or `URL_DELETED` (removed).
3. The run log prints an `OK`/`FAIL` line per URL.

## Option B — Run locally

Requires `python3` and `openssl` (both standard on macOS/Linux). No `pip install` needed.

```bash
# Put the downloaded key here (this path is git-ignored):
mv ~/Downloads/your-key.json scripts/google-indexing/service-account.json

# Submit every URL in urls.txt:
python3 scripts/google-indexing/submit.py

# Or submit specific URLs:
python3 scripts/google-indexing/submit.py https://fulcrumgrid.com/products/

# Or point at a key elsewhere:
python3 scripts/google-indexing/submit.py --key /path/to/key.json
```

You can also pass the key via env var instead of the file — a path or the raw JSON:

```bash
export GOOGLE_INDEXING_SA_KEY="$(cat /path/to/key.json)"
python3 scripts/google-indexing/submit.py
```

---

## Everyday use

- Edit [`urls.txt`](./urls.txt) whenever you publish or substantially change pages,
  then run the script / Action.
- Daily quota is **200 URLs per project** by default.
- **Never commit the key.** `service-account.json` (and any `*.json` here) is
  git-ignored; for CI it lives only in the `GOOGLE_INDEXING_SA_KEY` secret.

## Troubleshooting

- `403 Permission denied` — the service account isn't an **Owner** of the property
  in Search Console (step 4), or you added the wrong email.
- `403 ... has not been used in project ... or it is disabled` — the Indexing API
  isn't enabled for that project (step 2).
- `429 / quota exceeded` — you hit the 200/day limit; try again tomorrow.
