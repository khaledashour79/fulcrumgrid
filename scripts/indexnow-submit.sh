#!/usr/bin/env bash
# IndexNow submitter for fulcrumgrid.com
#
# Notifies IndexNow-enabled search engines (Bing, Yandex, Seznam, Naver, etc.)
# that URLs are new or changed, so they crawl them sooner.
#
# Usage:
#   scripts/indexnow-submit.sh                      # submit every URL in sitemap.xml
#   scripts/indexnow-submit.sh https://fulcrumgrid.com/blog/new-post/  ...   # submit specific URLs
#
# Notes:
#   - Submit only NEW or CHANGED URLs in normal use; the no-arg mode (whole
#     sitemap) is meant for the initial announcement, not routine pinging.
#   - One IndexNow ping fans out to all participating engines automatically.
set -euo pipefail

HOST="fulcrumgrid.com"
KEY="5b460af7e73dd0dc0e84678eb37b64a0"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
ENDPOINT="https://api.indexnow.org/indexnow"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Collect URLs: explicit args, else every <loc> in sitemap.xml
if [ "$#" -gt 0 ]; then
  URLS=("$@")
else
  mapfile -t URLS < <(grep -oE '<loc>[^<]+</loc>' "${ROOT}/sitemap.xml" | sed -E 's#</?loc>##g')
fi

if [ "${#URLS[@]}" -eq 0 ]; then
  echo "No URLs to submit." >&2
  exit 1
fi

# Build the JSON urlList
url_json="$(printf '"%s",' "${URLS[@]}")"
url_json="[${url_json%,}]"

payload=$(cat <<JSON
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": ${url_json}
}
JSON
)

echo "Submitting ${#URLS[@]} URL(s) to IndexNow..."
http_code=$(curl -sS -o /tmp/indexnow_resp.txt -w '%{http_code}' \
  -X POST "${ENDPOINT}" \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data "${payload}")

echo "HTTP ${http_code}"
# 200 = accepted; 202 = accepted, key validation pending; 4xx = problem
case "${http_code}" in
  200|202) echo "OK — search engines notified." ;;
  *) echo "Response body:"; cat /tmp/indexnow_resp.txt; exit 1 ;;
esac
