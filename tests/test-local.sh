#!/bin/bash
# Quick test script for local testing

echo "=========================================="
echo "Testing Documentation Update Script"
echo "=========================================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 not found"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python version: $PYTHON_VERSION"

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements-ci.txt

echo ""
echo "Running sync pipeline with fail-on-diff..."
echo "=========================================="
python3 tools/v1_sync_pipeline/sync_v1_docs.py --fail-on-diff || true

echo ""
echo "Running link checker..."
python3 tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md

echo ""
echo "=========================================="
echo "Test complete!"
echo ""
echo "To regenerate docs after inspecting diffs, run:"
echo "  python3 tools/v1_sync_pipeline/sync_v1_docs.py"
echo "=========================================="
