# Repository Structure Best Practices

This document explains the repository structure and why files are organized this way.

## Directory Structure

### `.github/` - GitHub-Specific Configuration

- **Purpose**: Contains GitHub-specific configuration files
- **Contents**:
  - `workflows/` - GitHub Actions workflow definitions
  - `scripts/` - Scripts used specifically by CI/CD workflows
  - `docs-version-*.json` - Workflow state/metadata files

**Why here?**: These files are specifically for GitHub Actions and CI/CD. Keeping them in `.github/` makes it clear they're GitHub-specific.

### `tests/` - Test Files

- **Purpose**: Contains all test scripts and test-related files
- **Contents**:
  - Test scripts (`.sh`, `.py`)
  - Test documentation (`README.md`)

**Why here?**: Standard practice - test files belong in a `tests/` directory at the repository root, not in `.github/`.

### `docs/development/` - Development Documentation

- **Purpose**: Documentation for developers working on the project
- **Contents**:
  - `TESTING.md` - Testing guide
  - `TEST_RESULTS.md` - Test results summary

**Why here?**: Development documentation belongs in `docs/`, separate from user-facing documentation.

### `requirements-ci.txt` - CI Dependencies

- **Purpose**: Python dependencies needed for CI/CD workflows
- **Location**: Repository root

**Why here?**: Standard practice - requirements files are typically at the repository root. The `-ci` suffix indicates it's for CI/CD.

## Best Practices Followed

1. ✅ **Tests in `tests/`** - Not in `.github/`
2. ✅ **Documentation in `docs/`** - Organized by purpose
3. ✅ **Requirements at root** - Standard location
4. ✅ **GitHub configs in `.github/`** - GitHub-specific files
5. ✅ **Clear separation** - Each directory has a clear purpose

## File Locations Summary

| File Type | Location | Reason |
|-----------|----------|--------|
| Test scripts | `tests/` | Standard practice |
| Test docs | `docs/development/` | Development docs |
| CI scripts | `.github/scripts/` | GitHub-specific |
| Workflows | `.github/workflows/` | GitHub Actions |
| Requirements | `requirements-ci.txt` | Root level, CI-specific |
| Metadata | `.github/docs-version-*.json` | Workflow state |
