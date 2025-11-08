#!/usr/bin/env python3
"""
Validate documentation structure and metadata files.

This script checks:
- Documentation directories exist (docs/v1/, docs/v2/)
- Version metadata files are valid
- Required files are present
"""
import json
import sys
from pathlib import Path


def validate_docs_structure() -> bool:
    """Validate the documentation directory structure."""
    errors = []
    warnings = []

    # Check docs directory exists
    docs_dir = Path("docs")
    if not docs_dir.exists():
        errors.append("docs/ directory does not exist")
        return False

    # Check v1 directory
    v1_dir = docs_dir / "v1"
    if not v1_dir.exists():
        warnings.append("docs/v1/ directory does not exist (expected for v1 docs)")
    else:
        v1_doc = v1_dir / "affinity_api_docs.md"
        if not v1_doc.exists():
            warnings.append("docs/v1/affinity_api_docs.md does not exist")

    # Check v2 directory (optional, may not exist yet)
    v2_dir = docs_dir / "v2"
    if not v2_dir.exists():
        # This is OK, v2 may not be implemented yet
        pass

    # Check version metadata files
    github_dir = Path(".github")
    if github_dir.exists():
        v1_metadata = github_dir / "docs-version-v1.json"
        v2_metadata = github_dir / "docs-version-v2.json"

        for metadata_file in [v1_metadata, v2_metadata]:
            if metadata_file.exists():
                try:
                    with open(metadata_file) as f:
                        data = json.load(f)
                        # Validate structure
                        required_keys = ["api_version", "source_url"]
                        for key in required_keys:
                            if key not in data:
                                errors.append(
                                    f"{metadata_file} missing required key: {key}"
                                )
                except json.JSONDecodeError as e:
                    errors.append(f"{metadata_file} is not valid JSON: {e}")

    # Report results
    if errors:
        print("ERRORS found:")
        for error in errors:
            print(f"  ✗ {error}")

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  ⚠ {warning}")

    if errors:
        return False

    if warnings:
        print("Structure validation completed with warnings (non-fatal)")

    return True


if __name__ == "__main__":
    success = validate_docs_structure()
    sys.exit(0 if success else 1)
