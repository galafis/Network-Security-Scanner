# Contributing to Network Security Scanner

First off, thank you for considering contributing to Network Security Scanner! It's people like you that make this tool better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to fostering an open and welcoming environment. Be respectful, inclusive, and constructive in all interactions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone your fork:**
```bash
git clone https://github.com/YOUR-USERNAME/Network-Security-Scanner.git
cd Network-Security-Scanner
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
```

5. **Run tests to verify setup:**
```bash
python3 -m pytest -v
```

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Python version, etc.)
- **Error messages** or logs if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the proposed functionality
- **Explain why this enhancement would be useful**
- **Include examples** of how it would work

### Code Contributions

We love code contributions! Here's how:

1. **Find or create an issue** describing what you want to work on
2. **Comment on the issue** to let others know you're working on it
3. **Create a branch** from `main` with a descriptive name
4. **Write your code** following our coding standards
5. **Add tests** for new functionality
6. **Update documentation** if needed
7. **Submit a pull request**

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: Maximum 100 characters (soft limit 88 for Black compatibility)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Grouped and sorted (standard library, third-party, local)
- **Docstrings**: Required for all public functions, classes, and modules
- **Type hints**: Encouraged for function signatures

### Code Quality

- **Write clear, self-documenting code**
- **Add comments for complex logic**
- **Keep functions focused** on a single responsibility
- **Avoid code duplication** - use helper functions
- **Handle errors gracefully** with proper exception handling

### Documentation

- **Docstrings**: Use Google-style docstrings
- **Comments**: Explain "why", not "what"
- **README**: Update if you change functionality
- **Examples**: Provide usage examples for new features

Example docstring:
```python
def scan_host(self, host, ports=None, timeout=1):
    """Scan a single host for open ports.
    
    Args:
        host (str): Hostname or IP address to scan
        ports (list, optional): List of ports to scan. Defaults to common_ports.
        timeout (int, optional): Socket timeout in seconds. Defaults to 1.
    
    Returns:
        dict: Scan results containing open ports, services, and vulnerabilities
    
    Raises:
        ValueError: If host format is invalid
    
    Example:
        >>> scanner = NetworkScanner()
        >>> results = scanner.scan_host("example.com", ports=[80, 443])
        >>> print(results['open_ports'])
        [80, 443]
    """
```

## Testing Guidelines

### Writing Tests

- **Unit tests** for individual functions and methods
- **Integration tests** for API endpoints and workflows
- **Test edge cases** and error conditions
- **Mock external dependencies** (network calls, file I/O)
- **Descriptive test names** that explain what is being tested

### Running Tests

```bash
# Run all tests
python3 -m pytest -v

# Run specific test file
python3 -m pytest test_network_scanner.py -v

# Run with coverage
python3 -m pytest --cov=network_scanner --cov=app --cov-report=html

# Run specific test
python3 -m pytest test_app.py::TestFlaskApp::test_health_endpoint -v
```

### Test Coverage

- **Aim for >80% code coverage** for new code
- **All new features** must include tests
- **Bug fixes** should include regression tests

## Commit Messages

We follow the Conventional Commits specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring (no feature change)
- **test**: Adding or updating tests
- **chore**: Build process or tooling changes

### Examples

```
feat(scanner): add UDP port scanning capability

Implement UDP scanning using socket DGRAM type.
Includes timeout handling and service identification.

Closes #42
```

```
fix(api): validate IP address format before scanning

Added regex validation to prevent invalid IP addresses
from being processed. Returns 400 error with helpful message.

Fixes #123
```

## Pull Request Process

### Before Submitting

1. **Update your branch** with the latest `main`
2. **Run all tests** and ensure they pass
3. **Check code style** (consider using `black` and `flake8`)
4. **Update documentation** if needed
5. **Add your changes** to a feature branch

### PR Description

Include in your PR description:

- **Summary** of changes
- **Motivation** for the changes
- **Related issues** (use "Fixes #123" or "Closes #123")
- **Testing done** to verify changes
- **Screenshots** for UI changes

### Review Process

1. **Automated checks** must pass (tests, linting)
2. **Code review** by at least one maintainer
3. **Address feedback** by updating your PR
4. **Squash commits** if requested
5. **Merge** once approved

### After Merge

- **Delete your feature branch**
- **Close related issues** if not automatically closed
- **Celebrate** your contribution! 🎉

## Additional Notes

### Security Issues

**Do NOT open public issues for security vulnerabilities.** Instead:

1. Email the maintainer directly (see README for contact)
2. Provide detailed information about the vulnerability
3. Allow time for a fix before public disclosure

### License

By contributing, you agree that your contributions will be licensed under the MIT License.

### Questions?

Feel free to open an issue with the "question" label or reach out to the maintainers.

---

Thank you for contributing to Network Security Scanner! 🛡️
