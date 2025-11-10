#!/bin/bash
# Edge case smoke tests for the v1 sync pipeline.

set -euo pipefail

echo "=========================================="
echo "Edge Case Testing Suite (sync_v1_docs.py)"
echo "=========================================="
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

echo "Test 1: Fail-on-diff behavior"
echo "----------------------------------------"
set +e
python3 tools/v1_sync_pipeline/sync_v1_docs.py --fail-on-diff
STATUS=$?
set -e
if [ "$STATUS" -eq 0 ]; then
  echo "✓ No diff detected"
elif [ "$STATUS" -eq 1 ]; then
  echo "✓ Diff detected (expected if live site changed)"
else
  echo "✗ Unexpected exit code: $STATUS"
  exit "$STATUS"
fi
echo ""

echo "Test 2: Invalid URL handling"
echo "----------------------------------------"
set +e
python3 tools/v1_sync_pipeline/sync_v1_docs.py --url https://invalid.affinity.local --fail-on-diff >/tmp/sync_invalid.log 2>&1
INVALID_STATUS=$?
set -e
if [ "$INVALID_STATUS" -ne 0 ]; then
  echo "✓ Script fails fast for invalid sources"
else
  echo "✗ Expected failure for invalid URL"
  exit 1
fi
echo ""

echo "Test 3: Link checker dry run"
echo "----------------------------------------"
python3 tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md
echo ""

echo "Test 4: Dependency sanity check"
echo "----------------------------------------"
python3 -c "import bs4, requests; print('✓ BeautifulSoup + requests available')"
echo ""

echo "Test 5: Snapshot directory writable"
echo "----------------------------------------"
python3 - <<'PY'
from pathlib import Path
path = Path('tmp/snapshots')
path.mkdir(parents=True, exist_ok=True)
print(f'✓ Snapshot dir ready at {path.resolve()}')
PY
echo ""

echo "=========================================="
echo "Edge Case Testing Complete"
echo "=========================================="
