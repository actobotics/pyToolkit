# Contributing to pytoolkit

Thank you for your interest in contributing to pytoolkit! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with the community. We aim to create a welcoming environment for all contributors.

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pytoolkit --cov-report=html

# Run specific test file
pytest tests/test_cache.py

# Run with verbose output
pytest -v
```

### Code Formatting and Linting

```bash
# Format code with Black
black src tests

# Check code style with Ruff
ruff check src tests

# Auto-fix issues
ruff check --fix src tests

# Type checking with MyPy
mypy src/pytoolkit
```

### Pre-commit Hooks

Pre-commit hooks will automatically run Black and Ruff before each commit:

```bash
# Run manually on all files
pre-commit run --all-files
```

## Coding Standards

### Python Style

- Follow PEP 8 guidelines
- Use Black for code formatting (line length: 100)
- Use type hints for all function signatures
- Write descriptive docstrings (NumPy style)

### Example Function

```python
from typing import Optional


def example_function(param1: str, param2: int = 10) -> Optional[str]:
    """Brief description of what the function does.

    Parameters
    ----------
    param1 : str
        Description of param1
    param2 : int, optional
        Description of param2, by default 10

    Returns
    -------
    Optional[str]
        Description of return value

    Examples
    --------
    >>> example_function("test")
    'result'

    Raises
    ------
    ValueError
        If param1 is empty
    """
    if not param1:
        raise ValueError("param1 must not be empty")
    
    # Implementation here
    return f"{param1}_{param2}"
```

### Testing Guidelines

- Write tests for all new features
- Aim for 80%+ code coverage
- Use descriptive test names: `test_function_name_behavior`
- Group related tests in classes
- Use fixtures for common setup

### Example Test

```python
import unittest
from pytoolkit.example import example_function


class TestExampleFunction(unittest.TestCase):
    def test_example_function_basic(self):
        """Test basic functionality."""
        result = example_function("test")
        self.assertEqual(result, "test_10")

    def test_example_function_custom_param(self):
        """Test with custom parameter."""
        result = example_function("test", param2=20)
        self.assertEqual(result, "test_20")

    def test_example_function_empty_input(self):
        """Test that empty input raises ValueError."""
        with self.assertRaises(ValueError):
            example_function("")
```

## Commit Messages

Write clear, descriptive commit messages:

```
Type: Brief description (50 chars or less)

More detailed explanation if necessary. Wrap at 72 characters.
Explain what changed and why, not how.

- Bullet points are okay
- Use present tense: "Add feature" not "Added feature"

Closes #123
```

### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat: Add async HTTP client module

Implements an async version of HttpClient using aiohttp.
Supports all standard HTTP methods with retry logic.

Closes #45
```

```
fix: Handle unpicklable objects in cache decorator

Falls back to string representation when pickle fails.
Adds test case for unpicklable objects.

Fixes #78
```

## Pull Request Process

1. **Update Tests**: Ensure all tests pass and add new tests for your changes
2. **Update Documentation**: Update docstrings, README, and docs if needed
3. **Update CHANGELOG**: Add your changes to the `[Unreleased]` section
4. **Run All Checks**: Make sure linting, type checking, and tests pass
5. **Create PR**: Use the PR template and fill in all sections
6. **Respond to Feedback**: Address review comments promptly

### PR Checklist

- [ ] Tests pass locally
- [ ] Code is formatted with Black
- [ ] No linting errors from Ruff
- [ ] Type checking passes with MyPy
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Commit messages are clear
- [ ] PR description is complete

## Adding New Modules

When adding a new module to pytoolkit:

1. **Create the module**: `src/pytoolkit/your_module.py`
2. **Add type hints**: All functions should have full type annotations
3. **Write docstrings**: Use NumPy style with examples
4. **Create tests**: `tests/test_your_module.py` with good coverage
5. **Update `__init__.py`**: Export main functions/classes if appropriate
6. **Update README**: Add module to the features list
7. **Update CHANGELOG**: Document the new module

## Documentation

### Building Docs Locally

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Build HTML documentation
cd docs
make html

# View in browser
open _build/html/index.html  # macOS
# or
start _build/html/index.html  # Windows
```

### Writing Documentation

- Use clear, concise language
- Include code examples
- Link to related functions/modules
- Add examples to docstrings

## Questions?

If you have questions:

- Check existing issues and discussions
- Review the documentation
- Ask in a new issue with the `question` label

## Recognition

Contributors will be recognized in:
- CHANGELOG.md (for significant contributions)
- GitHub contributors page
- Release notes

Thank you for contributing to pytoolkit! 🎉

