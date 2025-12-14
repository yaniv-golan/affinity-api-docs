# Affinity API Documentation (Markdown Copy)

[![Tests](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/tests.yml/badge.svg)](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/tests.yml)
[![Pre-commit](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/pre-commit.yml)
[![Documentation Updates](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/check-docs-updates.yml/badge.svg)](https://github.com/yaniv-golan/affinity-api-docs/actions/workflows/check-docs-updates.yml)

This repository contains markdown versions of the official Affinity API documentation, making it easier to work with AI coding assistants and other tools that prefer static, text-based documentation.

## Official Documentation

**⚠️ Important:** The official and authoritative Affinity API documentation is maintained by Affinity at:

- **API v1 (Legacy):** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
- **API v2 (Current):** [https://developer.affinity.co/](https://developer.affinity.co/)

**Always refer to the official Affinity documentation for the most up-to-date and accurate information.**

## Purpose

The original Affinity API documentation is hosted on dynamic, interactive websites that can be challenging to work with when using AI coding assistants, documentation parsers, or other automated tools. This repository provides:

- **Static markdown format** that's easier to search, parse, and reference
- **Better compatibility** with AI coding assistants and language models
- **Offline access** to API documentation
- **Version control** to track changes and updates over time
- **Direct raw access** via GitHub raw URLs for programmatic use
- **llms.txt format** - Standardized index format for LLM/IDE integration

## Quick Access

### llms.txt Format (Recommended for IDEs)

- 📋 [llms.txt](llms.txt) - Standardized index format for LLMs and IDEs (Cursor, Windsurf, Claude)
  - Follows [LangGraph llms.txt specification](https://langchain-ai.github.io/langgraph/llms-txt-overview/)
  - Provides links to full documentation
  - Optimized for IDE integration and MCP servers

### Raw Markdown Files (Direct Links)

**API v1 Documentation:**

- 📄 [View on GitHub](https://github.com/yaniv-golan/affinity-api-docs/blob/main/docs/v1/affinity_api_docs.md)
- 🔗 [Raw Markdown](https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md) (for AI tools, parsers, curl, wget)

**API v2 Documentation:**

- 📄 [View on GitHub](https://github.com/yaniv-golan/affinity-api-docs/blob/main/docs/v2/affinity_api_docs.md)
- 🔗 [Raw Markdown](https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v2/affinity_api_docs.md)
- 🔗 [OpenAPI JSON](https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v2/openapi.json)

### Accessing Raw Markdown

**For AI Coding Assistants:**

- Use the `llms.txt` file for IDE integration (recommended)
- Or use the raw GitHub URL above for direct access
- The raw markdown format is optimized for AI parsing and reference

**For Command Line:**

```bash
# Download using curl
curl -O https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md

# Download using wget
wget https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md

# View directly
curl https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md
```

**For Git Clone:**

```bash
git clone https://github.com/yaniv-golan/affinity-api-docs.git
cd affinity-api-docs/docs/v1
# Files are now available locally
```

## Current Status

### API v1 Documentation

- ✅ Core documentation auto-generated from https://api-docs.affinity.co/
- ✅ Formatting standardized (tables, fenced `bash` and `json` blocks today; parser auto-detects additional languages if Affinity adds them)
- ✅ Code examples + JSON request/response samples embedded for every endpoint section
- ✅ Raw markdown accessible via direct links
- 📂 Location: `docs/v1/affinity_api_docs.md` (do **not** edit manually)

### API v2 Documentation

- ✅ Auto-generated from https://developer.affinity.co/ via the new v2 sync pipeline
- ✅ Tag-based chapters, request/response tables, schema appendix, and error reference
- ✅ Example `curl` requests synthesized for every endpoint
- 📂 Location: `docs/v2/affinity_api_docs.md` (do **not** edit manually)
- 📂 OpenAPI spec: `docs/v2/openapi.json` (do **not** edit manually)

## Automated Updates & Manual Workflow

### GitHub Actions

- **Sync Affinity Docs** (`.github/workflows/check-docs-updates.yml`)
  - Runs daily at 00:00 UTC (plus manual `workflow_dispatch`)
  - Executes both sync pipelines and link-checks the generated markdown
  - Uses `peter-evans/create-pull-request` to open a PR whenever the generated outputs change
- **Tests** (`.github/workflows/tests.yml`)
  - Runs on push/PR
  - Re-runs the sync script with `--fail-on-diff` to ensure the repo already contains the generated output
  - Executes the pytest suite (coverage over `tools/v1_sync_pipeline` and `tools/v2_sync_pipeline`)

### Manual Sync Steps

When working locally (or verifying CI results):

```bash
# v1 workflow
python tools/v1_sync_pipeline/sync_v1_docs.py
python tools/v1_sync_pipeline/qa/check_links.py docs/v1/affinity_api_docs.md

# v2 workflow
python tools/v2_sync_pipeline/sync_v2_docs.py
python tools/v1_sync_pipeline/qa/check_links.py docs/v2/affinity_api_docs.md

# Shared test suite
python -m pytest
```

All generated artifacts (HTML snapshots, extracted code blocks, metadata) are written under `tmp/` and ignored by git. Commit only the updated markdown + metadata that land outside `tmp/`.

#### Example Overrides & Validation

- Manual fixes for specific endpoints live in `tools/v1_sync_pipeline/example_overrides.yml`. Each entry can override the Example Request/Response blocks for a section when the live site is inaccurate.
- `python tools/v1_sync_pipeline/sync_v1_docs.py` now validates that every Example Request matches the section verb/path. Any mismatches are written to `tmp/v1_sync_metadata.json` and echoed to the workflow summary.
- If a mismatch is intentional (for example, until the upstream docs are corrected), add or update the corresponding override entry instead of editing the markdown directly.

### Disabling the Schedule

If you need to pause the daily sync, edit `.github/workflows/check-docs-updates.yml` and remove/comment the `schedule` block. Manual dispatch remains available.

## Disclaimer

**Use at your own risk.** While every effort is made to ensure accuracy and keep this documentation synchronized with the official Affinity documentation, this is an unofficial copy and may contain errors, omissions, or outdated information.

For production use or critical implementations, always verify against the [official Affinity API documentation](https://developer.affinity.co/).

## Repository Structure

```
affinity-api-docs/
├── README.md              # This file
├── CHANGELOG.md           # Repository changelog
├── AGENTS.md              # Developer/AI agent guidelines
├── llms.txt               # llms.txt format index for LLMs/IDEs
├── requirements-ci.txt    # Python dependencies for CI/CD
├── .github/
│   ├── workflows/        # GitHub Actions workflows
│   │   ├── check-docs-updates.yml  # Daily sync + auto-PR
│   │   ├── pre-commit.yml          # Pre-commit checks
│   │   └── tests.yml               # Test suite
│   └── scripts/
│       └── validate_docs_structure.py
├── docs/
│   ├── v1/               # API v1 documentation
│   │   └── affinity_api_docs.md        # Auto-generated canonical doc
│   ├── v2/               # API v2 documentation
│   │   ├── affinity_api_docs.md        # Auto-generated canonical doc
│   │   └── openapi.json                # Auto-generated OpenAPI spec
│   └── development/      # Development documentation
│       ├── TESTING.md    # Testing guide
│       └── TEST_RESULTS.md  # Test results
│   └── (local only) docs/internal/     # Gitignored planning notes (kept outside repo)
├── tools/
│   └── v1_sync_pipeline/
│       ├── sync_v1_docs.py
│       └── qa/
│           ├── check_links.py
│           └── compare_to_live.py
├── tests/                # Test suite (pytest)
│   ├── README.md         # Test documentation
│   ├── conftest.py      # Pytest fixtures
│   ├── test_documentation_updates.py  # Main test suite
│   ├── test-local.sh    # Legacy test script
│   ├── test-edge-cases.sh  # Legacy test script
│   ├── test-production-scenarios.sh  # Legacy test script
│   └── test-realistic-scenarios.py  # Legacy test script
├── pytest.ini           # Pytest configuration
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── .markdownlint.json    # Markdown linting rules
├── .yamllint.yml         # YAML linting configuration
├── pyproject.toml        # Python tooling configuration
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Contribution guidelines
├── internal_docs/        # Planning + reports
└── tmp/                  # Gitignored snapshots/artifacts
```

> **Note:** The `docs/internal/` path is intentionally gitignored. Keep any private rollout plans or personal notes there locally without committing them to the public repository.

## Authentication

- **API v1:** Supports HTTP Basic Auth (API key as password, no username) or Bearer token
- **API v2:** Requires Bearer token authentication only

See the individual documentation files for detailed authentication instructions.

## Development

### Python Version

This project targets **Python 3.11.4**. We recommend using [pyenv](https://github.com/pyenv/pyenv) to match the interpreter used in CI/CD:

```bash
# install pyenv (see https://github.com/pyenv/pyenv#installation for details)
brew install pyenv  # macOS example

# install and activate Python 3.11.4
pyenv install 3.11.4
pyenv local 3.11.4

# verify
python --version  # -> Python 3.11.4
```

All project scripts (`tools/*_sync_pipeline/*.py`, tests, pre-commit) assume this interpreter. If you use a different Python version, you may see SSL/tooling warnings that CI does not cover.

### Pre-commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) hooks to ensure code quality and consistency.

**Setup**:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run on all files (optional)
pre-commit run --all-files
```

**What's checked**:

- Python code formatting (black, isort, ruff)
- Markdown linting (markdownlint)
- YAML/JSON validation
- Documentation structure validation
- Trailing whitespace and end-of-file fixes

Hooks run automatically on `git commit`. They also run in CI/CD on every PR.

For more details, see [Pre-commit Hooks Guide](docs/development/PRE_COMMIT.md).

### Testing

See [Testing Guide](docs/development/TESTING.md) for details on running tests.

### Dependency Management

This repository uses [Dependabot](https://docs.github.com/en/code-security/dependabot) to automatically keep dependencies up to date:

- **Python packages**: Checked weekly (Mondays)
- **GitHub Actions**: Checked monthly

Dependabot will automatically create pull requests for dependency updates. Review and merge these PRs to keep dependencies current.

## Contributing

If you notice discrepancies between this documentation and the official Affinity documentation, please:

1. Verify against the [official documentation](https://developer.affinity.co/)
2. Open an issue describing the discrepancy
3. If possible, submit a pull request with corrections

**Note**: All PRs are automatically checked by pre-commit hooks. Please ensure your code passes these checks before submitting.

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of repository infrastructure changes and improvements.

**Note**: The changelog tracks repository changes (CI/CD, features, improvements). Individual documentation updates from the official Affinity API are tracked in Pull Requests.

## License

This repository is licensed under the MIT License - see [LICENSE](LICENSE) for details.

**Note**: This is an unofficial documentation copy. The original Affinity API documentation and all associated intellectual property rights belong to Affinity. This repository is maintained for convenience and educational purposes only.

## Contact

For API support or questions about the Affinity API itself, contact Affinity directly:

- **Affinity Support:** support@affinity.co
- **Official Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)

## Acknowledgments

All content is derived from the official Affinity API documentation. This repository simply provides an alternative format for easier consumption by development tools and AI assistants.
