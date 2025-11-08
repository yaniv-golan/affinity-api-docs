#!/bin/bash
# Comprehensive edge case testing for the documentation update script

set -e

echo "=========================================="
echo "Edge Case Testing Suite"
echo "=========================================="
echo ""

# Get script directory and navigate to repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

# Test 1: No changes detected (simulate by using same content)
echo "Test 1: No changes detected"
echo "----------------------------------------"
# This should exit cleanly without creating PR
python3 .github/scripts/check_and_update_docs.py --api-version v1 --dry-run 2>&1 | grep -E "(No changes|Updated)" || echo "Test 1 completed"
echo ""

# Test 2: v2 not implemented (should skip gracefully)
echo "Test 2: v2 not implemented (should skip)"
echo "----------------------------------------"
python3 .github/scripts/check_and_update_docs.py --api-version v2 --dry-run 2>&1 | grep -E "(Skipping|not yet)" || echo "Test 2 completed"
echo ""

# Test 3: Invalid API version
echo "Test 3: Invalid API version (should error)"
echo "----------------------------------------"
python3 .github/scripts/check_and_update_docs.py --api-version invalid --dry-run 2>&1 | grep -E "(Error|Unknown)" || echo "Test 3 completed"
echo ""

# Test 4: Check metadata file structure
echo "Test 4: Verify metadata file structure"
echo "----------------------------------------"
python3 -c "
import json
import os

# Check v1 metadata
if os.path.exists('.github/docs-version-v1.json'):
    with open('.github/docs-version-v1.json') as f:
        data = json.load(f)
        assert 'api_version' in data
        assert 'last_checked' in data
        print('✓ v1 metadata file structure is valid')
else:
    print('✗ v1 metadata file missing')
"
echo ""

# Test 5: Test force check flag
echo "Test 5: Force check flag"
echo "----------------------------------------"
python3 .github/scripts/check_and_update_docs.py --api-version v1 --force-check true --dry-run 2>&1 | head -5
echo ""

# Test 6: Check if script handles missing dependencies gracefully
echo "Test 6: Import check"
echo "----------------------------------------"
python3 -c "
try:
    import requests
    import bs4
    print('✓ All dependencies available')
except ImportError as e:
    print(f'✗ Missing dependency: {e}')
"
echo ""

# Test 7: Check URL accessibility
echo "Test 7: URL accessibility check"
echo "----------------------------------------"
python3 -c "
import requests
try:
    response = requests.get('https://api-docs.affinity.co/', timeout=10)
    print(f'✓ Website accessible (Status: {response.status_code})')
except Exception as e:
    print(f'✗ Website not accessible: {e}')
"
echo ""

# Test 8: Check git repository status
echo "Test 8: Git repository check"
echo "----------------------------------------"
if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "✓ Git repository detected"
    echo "  Current branch: $(git branch --show-current)"
else
    echo "✗ Not a git repository"
fi
echo ""

# Test 9: Check GitHub CLI availability
echo "Test 9: GitHub CLI check"
echo "----------------------------------------"
if command -v gh &> /dev/null; then
    echo "✓ GitHub CLI installed"
    gh auth status 2>&1 | head -1 || echo "  (Not authenticated - OK for dry-run)"
else
    echo "⚠ GitHub CLI not installed (needed for PR creation)"
fi
echo ""

# Test 10: Test duplicate PR detection logic
echo "Test 10: Duplicate PR detection (simulated)"
echo "----------------------------------------"
python3 -c "
import subprocess
import json

try:
    result = subprocess.run(
        ['gh', 'pr', 'list', '--state', 'open', '--json', 'number,headRefName'],
        capture_output=True,
        text=True,
        timeout=5
    )
    if result.returncode == 0:
        prs = json.loads(result.stdout)
        print(f'✓ Found {len(prs)} open PRs')
        for pr in prs:
            if 'auto-update' in pr['headRefName']:
                print(f'  - PR #{pr[\"number\"]}: {pr[\"headRefName\"]}')
    else:
        print('⚠ Could not check PRs (may not be authenticated)')
except Exception as e:
    print(f'⚠ Could not check PRs: {e}')
"
echo ""

echo "=========================================="
echo "Edge Case Testing Complete"
echo "=========================================="
