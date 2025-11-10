# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-11-10

### Added

- Section-bounded parser that keeps example blocks scoped to their endpoints and records per-section metadata.
- Example validation + override pipeline (`tools/v1_sync_pipeline/example_overrides.yml`) with warnings emitted to `tmp/v1_sync_metadata.json` and the workflow summary.
- Pytest guard ensuring `example_mismatches` stays empty.

### Changed

- Normalized smart quotes and common typos, relabeled body/form parameter tables, and added the missing interaction/reminder notes.
- README/AGENTS document the override workflow and metadata expectations.

## [1.0.0] - 2025-11-08

### Added

- **llms.txt format support** - Added `llms.txt` index file for LLM/IDE integration (Cursor, Windsurf, Claude)
- **Automated documentation updates** - GitHub Actions workflow to automatically sync with official Affinity documentation
- **Pre-commit hooks** - Automated code quality checks (black, isort, ruff, markdownlint, yamllint)
- **Dependabot configuration** - Automated dependency updates for Python packages and GitHub Actions
- **Workflow status badges** - Visual CI/CD status indicators in README
- **Comprehensive test suite** - pytest-based test suite with unit and integration tests
- **LICENSE file** - MIT License for the repository
- **CONTRIBUTING.md** - Contribution guidelines for contributors
- **Security policy** - `.github/SECURITY.md` for security vulnerability reporting
- **Repository structure documentation** - `REPOSITORY_STRUCTURE.md` explaining file organization
- **Development documentation** - Testing guide, pre-commit guide, and development docs
- **Raw markdown accessibility** - Direct links and instructions for accessing raw markdown files

### Changed

- **Workflow dependencies** - Optimized `check-docs-updates.yml` to run tests before documentation updates
- **Test script paths** - Fixed hardcoded paths in test scripts to use relative paths
- **README structure** - Updated repository structure diagram and added llms.txt references
- **Documentation header** - Automated header updates with synchronization timestamps

### Fixed

- Hardcoded absolute paths in test scripts
- README placeholder text (`YOUR_USERNAME`)
- Documentation structure inconsistencies

## [0.1.0] - 2025-11-06

### Added

- Initial extraction of Affinity API v1 documentation from official site
- Markdown formatting and cleanup
- Basic repository structure
- `.gitignore` configuration

---

**Note**: This changelog tracks repository infrastructure changes. Individual documentation updates from the official Affinity API documentation are tracked in Pull Requests and git commit history.
