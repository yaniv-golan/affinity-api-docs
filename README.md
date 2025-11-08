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

- 📋 Coming soon (planned)

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

- ✅ Core documentation extracted and cleaned
- ✅ Formatting standardized
- ✅ Raw markdown accessible via direct links
- ⚠️ **In Progress:** Adding code examples (cURL, Ruby, Python, Node.js)
- 📂 Location: `docs/v1/affinity_api_docs.md`

### API v2 Documentation

- 📋 **Planned:** Not yet started
- 📂 Location: `docs/v2/` (directory prepared)

## Automated Updates

This repository uses **automated GitHub Actions workflows** to keep the documentation synchronized with the official Affinity API documentation.

### How It Works

- **Schedule**: The workflow runs **daily at 00:00 UTC** to check for updates
- **Manual Trigger**: You can also manually trigger the workflow from the GitHub Actions tab in your repository
- **Process**:
  1. Fetches the latest documentation from the official Affinity websites
  2. Compares it with the current version in this repository
  3. If changes are detected, automatically creates a Pull Request (PR) with the updated documentation
  4. Adds a notice section to the documentation indicating that an update is available

### What to Expect

When an update is detected, you'll see:

- **A Pull Request** with the updated documentation
- **A notice section** at the top of the documentation file indicating:
  - The date the update was detected
  - A link to view the diff
  - A link to the PR
  - Status information

### Reviewing Updates

All automated updates require **manual review** before merging:

1. Review the PR to verify the changes match the official documentation
2. Check for any formatting issues
3. Ensure all code examples are present and correct
4. Merge the PR when satisfied

### Disabling Automated Updates

If you need to disable automated updates temporarily:

1. Edit `.github/workflows/check-docs-updates.yml`
2. Comment out or remove the `schedule` section
3. Commit the changes

### Workflow Details

- **Workflow File**: [`.github/workflows/check-docs-updates.yml`](.github/workflows/check-docs-updates.yml)
- **Script**: [`.github/scripts/check_and_update_docs.py`](.github/scripts/check_and_update_docs.py)
- **Version Tracking**: `.github/docs-version-v1.json` and `.github/docs-version-v2.json`
- **Testing**: See [Testing Guide](docs/development/TESTING.md) for details

The workflow supports both **v1** and **v2** API documentation (v2 will be enabled when that documentation is added to the repository).

## Disclaimer

**Use at your own risk.** While every effort is made to ensure accuracy and keep this documentation synchronized with the official Affinity documentation, this is an unofficial copy and may contain errors, omissions, or outdated information.

For production use or critical implementations, always verify against the [official Affinity API documentation](https://developer.affinity.co/).

## Repository Structure

```
affinity-api-docs/
├── README.md              # This file
├── CHANGELOG.md           # Repository changelog
├── AGENTS.md             # Developer/AI agent guidelines
├── llms.txt              # llms.txt format index for LLMs/IDEs
├── requirements-ci.txt   # Python dependencies for CI/CD
├── .github/
│   ├── workflows/        # GitHub Actions workflows
│   │   ├── check-docs-updates.yml  # Automated documentation updates
│   │   ├── pre-commit.yml          # Pre-commit checks
│   │   └── tests.yml               # Test suite
│   ├── scripts/          # CI/CD automation scripts
│   │   ├── check_and_update_docs.py
│   │   └── validate_docs_structure.py
│   ├── docs-version-v1.json  # Version tracking for v1
│   └── docs-version-v2.json  # Version tracking for v2
├── docs/
│   ├── v1/               # API v1 documentation
│   │   └── affinity_api_docs.md
│   ├── v2/               # API v2 documentation (planned)
│   └── development/      # Development documentation
│       ├── TESTING.md    # Testing guide
│       └── TEST_RESULTS.md  # Test results
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
└── .gitignore
```

## Authentication

- **API v1:** Supports HTTP Basic Auth (API key as password, no username) or Bearer token
- **API v2:** Requires Bearer token authentication only

See the individual documentation files for detailed authentication instructions.

## Development

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
