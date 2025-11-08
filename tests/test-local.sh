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
echo "Running script in DRY RUN mode..."
echo "=========================================="
python3 .github/scripts/check_and_update_docs.py --api-version v1 --dry-run

echo ""
echo "=========================================="
echo "Test complete!"
echo ""
echo "To test without dry-run (will create PRs):"
echo "  python3 .github/scripts/check_and_update_docs.py --api-version v1 --force-check true"
echo "=========================================="
