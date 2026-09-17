# CMS auth broker (one-time setup)

The content admin at `/admin/` logs in with GitHub. GitHub OAuth needs a tiny
server to swap the login `code` for a token (the client secret can't sit in the
browser). This folder is that server — a Cloudflare Worker, free tier.

You do this **once**. After that, editing is entirely in the browser.

## 1. Register a GitHub OAuth App
GitHub → **Settings → Developer settings → OAuth Apps → New OAuth App**:
- **Application name:** `FulcrumGrid CMS`
- **Homepage URL:** `https://fulcrumgrid.com`
- **Authorization callback URL:** `https://<your-worker-subdomain>.workers.dev/callback`
  (you'll get the exact worker URL in step 2 — you can come back and edit this)

Copy the **Client ID** and generate a **Client Secret**.

## 2. Deploy the Worker
From this folder:
```bash
npx wrangler login
npx wrangler deploy
npx wrangler secret put GITHUB_CLIENT_ID       # paste the Client ID
npx wrangler secret put GITHUB_CLIENT_SECRET   # paste the Client Secret
```
`wrangler deploy` prints the Worker URL (e.g. `https://fulcrumgrid-cms-oauth.<you>.workers.dev`).
Put that same URL as the callback URL in the GitHub OAuth App (step 1).

## 3. Point the CMS at it
In `admin/config.yml`, set:
```yaml
backend:
  base_url: https://fulcrumgrid-cms-oauth.<you>.workers.dev
```
Commit. Then open `https://fulcrumgrid.com/admin/`, click **Login with GitHub**,
and you're in. Only accounts with write access to the repo can save.

## How saving works
Saving in `/admin/` commits the content file to `main`. The **Deploy** GitHub
Action then rebuilds the affected pages from `/content/` and publishes them —
no local steps, no separate build.
