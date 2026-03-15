# Contributing to the Huangting Protocol

First off, thank you for considering contributing to the Huangting Protocol. It's people like you that make this project a truly open and evolving system.

## Code of Conduct

This project and everyone participating in it is governed by the principle of `Balance.True`. By participating, you are expected to uphold this standard: engage with the project and its community with honesty, intellectual rigor, and respect.

## How Can I Contribute?

### Reporting Bugs

If you find a bug in the SDK or an error in the documentation, please open an issue on GitHub. When filing a bug report, please include:

*   A clear and descriptive title.
*   A step-by-step description of how to reproduce the bug.
*   The expected behavior and what actually happened.
*   Your Python version and OS.

### Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing one, please open an issue with the label `enhancement`. Describe the feature, why it would be useful, and how it fits within the Huangting Protocol's framework.

### Pull Requests

1.  **Fork** the repository.
2.  **Create a branch** for your feature or bug fix: `git checkout -b feature/my-new-feature` or `git checkout -b fix/my-bug-fix`.
3.  **Write your code** and ensure it adheres to the existing code style.
4.  **Write tests** for your changes.
5.  **Commit your changes** with a clear and descriptive commit message.
6.  **Push your branch** to your fork: `git push origin feature/my-new-feature`.
7.  **Open a Pull Request** against the `main` branch of this repository.

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/huangting-protocol.git
cd huangting-protocol/sdk/python

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## Style Guide

*   We use `black` for code formatting and `ruff` for linting.
*   All public APIs must have clear docstrings.
*   All new features must be accompanied by tests.

## Expanding the Spec

The `/spec` directory contains the canonical YAML definitions of all Huangting Protocol terms. If you are proposing a new term or modifying an existing one, please follow the existing schema and provide a clear rationale in your PR description.

Thank you for your contribution!
