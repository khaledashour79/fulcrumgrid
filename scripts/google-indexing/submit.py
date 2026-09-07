#!/usr/bin/env python3
"""
Google Indexing API submitter for fulcrumgrid.com

Notifies Google that URLs are new/updated (or deleted) so it crawls them sooner,
using a service-account credential. Zero pip dependencies: uses only the Python
standard library plus the `openssl` CLI to sign the auth token.

Usage:
  # Submit every URL in urls.txt (default):
  python3 scripts/google-indexing/submit.py

  # Submit specific URLs:
  python3 scripts/google-indexing/submit.py https://fulcrumgrid.com/products/ https://fulcrumgrid.com/features/

  # Tell Google a URL was removed:
  python3 scripts/google-indexing/submit.py --type URL_DELETED https://fulcrumgrid.com/old-page/

Credential resolution (first match wins):
  1. --key <path>                         command-line flag
  2. $GOOGLE_INDEXING_SA_KEY              env var: either a file path OR the raw JSON
  3. scripts/google-indexing/service-account.json   (git-ignored; never commit it)

Notes:
  - The service-account email must be added as an Owner of the fulcrumgrid.com
    property in Google Search Console. See README.md for one-time setup.
  - Google's daily quota is 200 URLs per project by default.
  - Google officially supports this API for JobPosting/BroadcastEvent pages; for
    ordinary pages it may deprioritize submissions. Keep the sitemap + IndexNow
    (scripts/indexnow-submit.sh) as the primary channels.
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

SCOPE = "https://www.googleapis.com/auth/indexing"
PUBLISH_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_KEY = os.path.join(HERE, "service-account.json")
DEFAULT_URLS = os.path.join(HERE, "urls.txt")


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def die(msg: str, code: int = 1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def load_credentials(key_arg):
    """Return the parsed service-account dict from flag, env var, or default file."""
    raw = None
    source = None
    if key_arg:
        if not os.path.exists(key_arg):
            die(f"--key file not found: {key_arg}")
        raw = open(key_arg, encoding="utf-8").read()
        source = key_arg
    elif os.environ.get("GOOGLE_INDEXING_SA_KEY"):
        env = os.environ["GOOGLE_INDEXING_SA_KEY"].strip()
        if env.startswith("{"):
            raw = env
            source = "$GOOGLE_INDEXING_SA_KEY (inline JSON)"
        elif os.path.exists(env):
            raw = open(env, encoding="utf-8").read()
            source = env
        else:
            die("$GOOGLE_INDEXING_SA_KEY is set but is neither a path nor inline JSON")
    elif os.path.exists(DEFAULT_KEY):
        raw = open(DEFAULT_KEY, encoding="utf-8").read()
        source = DEFAULT_KEY
    else:
        die(
            "No service-account credential found. Provide one via --key, the "
            "GOOGLE_INDEXING_SA_KEY env var, or "
            f"{DEFAULT_KEY}\nSee scripts/google-indexing/README.md for setup."
        )
    try:
        sa = json.loads(raw)
    except json.JSONDecodeError as e:
        die(f"Credential is not valid JSON ({source}): {e}")
    for field in ("client_email", "private_key", "token_uri"):
        if field not in sa:
            die(f"Credential is missing '{field}' (is this a service-account key?)")
    print(f"Using service account: {sa['client_email']}")
    return sa


def sign_rs256(signing_input: str, private_key_pem: str) -> str:
    """Sign with RS256 using the openssl CLI (no crypto library needed)."""
    tf = tempfile.NamedTemporaryFile("w", suffix=".pem", delete=False)
    try:
        tf.write(private_key_pem)
        tf.close()
        proc = subprocess.run(
            ["openssl", "dgst", "-sha256", "-sign", tf.name],
            input=signing_input.encode("ascii"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode != 0:
            die(f"openssl signing failed: {proc.stderr.decode('utf-8', 'replace')}")
        return b64url(proc.stdout)
    finally:
        os.unlink(tf.name)


def get_access_token(sa: dict) -> str:
    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT"}
    claim = {
        "iss": sa["client_email"],
        "scope": SCOPE,
        "aud": sa["token_uri"],
        "iat": now,
        "exp": now + 3600,
    }
    signing_input = (
        b64url(json.dumps(header, separators=(",", ":")).encode())
        + "."
        + b64url(json.dumps(claim, separators=(",", ":")).encode())
    )
    jwt = signing_input + "." + sign_rs256(signing_input, sa["private_key"])
    body = urllib.parse.urlencode(
        {"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": jwt}
    ).encode()
    req = urllib.request.Request(
        sa["token_uri"], data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tok = json.loads(r.read())
    except urllib.error.HTTPError as e:
        die(f"Token request failed ({e.code}): {e.read().decode('utf-8', 'replace')}")
    except urllib.error.URLError as e:
        die(f"Token request network error: {e.reason}")
    if "access_token" not in tok:
        die(f"Token response missing access_token: {tok}")
    return tok["access_token"]


def publish(url: str, notify_type: str, token: str):
    body = json.dumps({"url": url, "type": notify_type}).encode()
    req = urllib.request.Request(
        PUBLISH_ENDPOINT, data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except urllib.error.URLError as e:
        return None, f"network error: {e.reason}"


def collect_urls(args) -> list:
    if args.urls:
        return args.urls
    path = args.urls_file or DEFAULT_URLS
    if not os.path.exists(path):
        die(f"No URLs given and URL list not found: {path}")
    urls = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            urls.append(line)
    if not urls:
        die(f"URL list is empty: {path}")
    return urls


def main():
    ap = argparse.ArgumentParser(description="Submit URLs to the Google Indexing API.")
    ap.add_argument("urls", nargs="*", help="URLs to submit (default: read urls.txt)")
    ap.add_argument("--key", help="Path to the service-account JSON key")
    ap.add_argument("--urls-file", help="File with one URL per line (default: urls.txt)")
    ap.add_argument("--type", default="URL_UPDATED",
                    choices=["URL_UPDATED", "URL_DELETED"],
                    help="Notification type (default: URL_UPDATED)")
    args = ap.parse_args()

    sa = load_credentials(args.key)
    urls = collect_urls(args)
    token = get_access_token(sa)

    print(f"\nSubmitting {len(urls)} URL(s) as {args.type} ...\n")
    ok = 0
    for u in urls:
        status, payload = publish(u, args.type, token)
        if status == 200:
            ok += 1
            when = payload.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "") if isinstance(payload, dict) else ""
            print(f"  OK    {u}  {when}")
        else:
            print(f"  FAIL  {u}  [{status}] {payload}")
    print(f"\nDone: {ok}/{len(urls)} accepted. (Google daily quota is 200 URLs/project.)")
    sys.exit(0 if ok == len(urls) else 2)


if __name__ == "__main__":
    main()
