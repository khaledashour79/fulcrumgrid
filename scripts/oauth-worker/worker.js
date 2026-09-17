// GitHub OAuth broker for Decap CMS, as a Cloudflare Worker.
//
// Decap's GitHub backend needs a tiny server to exchange the OAuth `code`
// for an access token (the client secret must never live in the browser).
// This Worker is that server. Deploy it once, set two secrets, and point
// admin/config.yml `base_url` at its URL.
//
// Secrets (set with `npx wrangler secret put ...`):
//   GITHUB_CLIENT_ID      — from your GitHub OAuth App
//   GITHUB_CLIENT_SECRET  — from your GitHub OAuth App

const AUTHORIZE = 'https://github.com/login/oauth/authorize';
const ACCESS_TOKEN = 'https://github.com/login/oauth/access_token';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const { pathname, searchParams, origin } = url;

    if (pathname === '/') {
      return new Response('FulcrumGrid CMS OAuth backend is running.', { status: 200 });
    }

    // Step 1 — Decap opens /auth; redirect the user to GitHub.
    if (pathname === '/auth') {
      const to = new URL(AUTHORIZE);
      to.searchParams.set('client_id', env.GITHUB_CLIENT_ID);
      to.searchParams.set('redirect_uri', `${origin}/callback`);
      to.searchParams.set('scope', searchParams.get('scope') || 'repo,user');
      to.searchParams.set('state', crypto.randomUUID());
      return Response.redirect(to.toString(), 302);
    }

    // Step 2 — GitHub redirects back to /callback with a code; exchange it
    // for a token and hand it to the Decap window via postMessage.
    if (pathname === '/callback') {
      const code = searchParams.get('code');
      const res = await fetch(ACCESS_TOKEN, {
        method: 'POST',
        headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify({
          client_id: env.GITHUB_CLIENT_ID,
          client_secret: env.GITHUB_CLIENT_SECRET,
          code,
        }),
      });
      const result = await res.json();
      const ok = !!result.access_token;
      const state = ok ? 'success' : 'error';
      const content = ok
        ? { token: result.access_token, provider: 'github' }
        : { error: result.error_description || result.error || 'Authentication failed' };

      const html = `<!doctype html><html><head><meta charset="utf-8"></head><body>
<script>
(function () {
  var message = 'authorization:github:${state}:' + JSON.stringify(${JSON.stringify(content)});
  function receive(e) {
    if (!e || !e.data || String(e.data).indexOf('authorizing:github') === -1) return;
    window.removeEventListener('message', receive, false);
    (e.source || window.opener).postMessage(message, e.origin || '*');
  }
  window.addEventListener('message', receive, false);
  (window.opener || window.parent).postMessage('authorizing:github', '*');
})();
</script>
</body></html>`;
      return new Response(html, { headers: { 'Content-Type': 'text/html; charset=utf-8' } });
    }

    return new Response('Not found', { status: 404 });
  },
};
