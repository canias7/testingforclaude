#!/bin/sh
# Download the page and print the text inside the first <title>…</title>.
set -eu
html=$(curl -sS -m 15 -L --fail https://example.com)
printf '%s\n' "$html" | sed -n 's/.*<title>\([^<]*\)<\/title>.*/\1/p' | head -n 1
