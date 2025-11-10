#!/bin/bash
# Production scenario smoke tests for the sync pipeline.

set -euo pipefail

echo "=========================================="
echo "Production Scenario Testing (sync pipeline)"
echo "=========================================="
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

echo "Scenario 1: Full regeneration"
echo "----------------------------------------"
python3 tools/v1_sync_pipeline/sync_v1_docs.py
echo "✓ Synced documentation"
echo ""

echo "Scenario 2: Verify canonical file + header"
echo "----------------------------------------"
if [ -f "docs/v1/affinity_api_docs.md" ]; then
  LINES=$(wc -l < docs/v1/affinity_api_docs.md)
  echo "✓ docs/v1/affinity_api_docs.md exists ($LINES lines)"
  if grep -q "Affinity API v1 Documentation (Auto-synced)" docs/v1/affinity_api_docs.md; then
    echo "✓ Auto-sync header present"
  else
    echo "⚠ Expected header not found"
  fi
else
  echo "✗ Canonical markdown missing"
  exit 1
fi
echo ""

echo "Scenario 3: Link checker + pytest"
echo "----------------------------------------"
python3 tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md
pytest tests/ -m "not integration" -k "test_" -q
echo ""

echo "Scenario 4: Metadata + snapshots"
echo "----------------------------------------"
if [ -f "tmp/v1_sync_metadata.json" ]; then
  python3 -c "import json; print('✓ Metadata:', json.load(open('tmp/v1_sync_metadata.json'))['output'])"
else
  echo "⚠ Metadata file missing (run sync again?)"
fi
SNAP_COUNT=$(ls tmp/snapshots 2>/dev/null | wc -l | tr -d ' ')
echo "Snapshots captured: ${SNAP_COUNT:-0}"
echo ""

echo "Scenario 5: Workflow YAML validation"
echo "----------------------------------------"
if command -v yamllint &> /dev/null; then
  yamllint .github/workflows/check-docs-updates.yml
  echo "✓ yamllint passed"
else
  echo "⚠ yamllint not installed locally; skipping"
fi
echo ""

echo "=========================================="
echo "Production Scenario Testing Complete"
echo "=========================================="
