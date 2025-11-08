# Affinity API Documentation (Markdown Copy)

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

## Current Status

### API v1 Documentation
- ✅ Core documentation extracted and cleaned
- ✅ Formatting standardized
- ⚠️ **In Progress:** Adding code examples (cURL, Ruby, Python, Node.js)
- 📂 Location: `docs/v1/affinity_api_docs.md`

### API v2 Documentation
- 📋 **Planned:** Not yet started
- 📂 Location: `docs/v2/` (directory prepared)

## Disclaimer

**Use at your own risk.** While every effort is made to ensure accuracy and keep this documentation synchronized with the official Affinity documentation, this is an unofficial copy and may contain errors, omissions, or outdated information. 

For production use or critical implementations, always verify against the [official Affinity API documentation](https://developer.affinity.co/).

## Repository Structure

```
affinity-api-docs/
├── README.md              # This file
├── AGENTS.md             # Developer/AI agent guidelines
├── docs/
│   ├── v1/               # API v1 documentation
│   │   └── affinity_api_docs.md
│   └── v2/               # API v2 documentation (planned)
└── .gitignore
```

## Authentication

- **API v1:** Supports HTTP Basic Auth (API key as password, no username) or Bearer token
- **API v2:** Requires Bearer token authentication only

See the individual documentation files for detailed authentication instructions.

## Contributing

If you notice discrepancies between this documentation and the official Affinity documentation, please:

1. Verify against the [official documentation](https://developer.affinity.co/)
2. Open an issue describing the discrepancy
3. If possible, submit a pull request with corrections

## License

This is an unofficial documentation copy. The original Affinity API documentation and all associated intellectual property rights belong to Affinity. This repository is maintained for convenience and educational purposes only.

## Contact

For API support or questions about the Affinity API itself, contact Affinity directly:
- **Affinity Support:** support@affinity.co
- **Official Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)

## Acknowledgments

All content is derived from the official Affinity API documentation. This repository simply provides an alternative format for easier consumption by development tools and AI assistants.

