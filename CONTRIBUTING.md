# Contributing to Geomatics

Thank you for considering contributing to the Geomatics Python package! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Changes](#submitting-changes)

---

## Code of Conduct

### Our Standards

- **Be respectful** and inclusive in all interactions
- **Welcome newcomers** and help them get started
- **Focus on constructive feedback** rather than criticism
- **Respect differing viewpoints** and experiences
- **Accept responsibility** and apologize when mistakes occur

### Scope

This Code of Conduct applies to all project spaces including issues, pull requests, and communications.

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating a bug report:
1. Check the existing issues to avoid duplicates
2. Collect information about the bug (Python version, OS, error messages)
3. Test with the latest version of the package

**When reporting a bug, include:**
- A clear, descriptive title
- Steps to reproduce the behavior
- Expected vs actual behavior
- Code samples if applicable
- Your environment details (Python version, OS)

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting features:
- Use a clear, descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- Provide examples of how it would be used
- Consider the scope (keep it focused on geomatics applications)

### 📝 Improving Documentation

Documentation improvements are highly valued:
- Fix typos or clarify confusing sections
- Add examples for existing functions
- Write tutorials for common use cases
- Translate documentation (if applicable)

### 🔧 Contributing Code

Areas where contributions are especially welcome:
- Additional coordinate transformation functions
- More geodetic calculations (distances, azimuths)
- Enhanced statistical tests for quality control
- Projection utilities (UTM, Web Mercator)
- Performance optimizations
- Bug fixes

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/geomatics.git
cd geomatics
```

### 2. Create a Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Development Dependencies

```bash
# Install package in development mode
pip install -e .

# Install development dependencies
pip install pytest numpy sympy
```

### 4. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

---

## Coding Standards

### Python Style Guide

Follow **PEP 8** guidelines:
- Use 4 spaces for indentation (no tabs)
- Limit lines to 79 characters for code, 72 for docstrings
- Use snake_case for function and variable names
- Use PascalCase for class names
- Add blank lines to separate logical sections

### Documentation Strings

All functions must have docstrings following NumPy style:

```python
def example_function(param1, param2):
    """
    Brief description of what the function does.
    
    More detailed explanation if needed. Describe the algorithm,
    special cases, or important considerations.
    
    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2
    
    Returns
    -------
    return_type
        Description of return value
    
    Examples
    --------
    >>> example_function(1, 2)
    3
    
    Notes
    -----
    Additional notes if needed
    
    References
    ----------
    .. [1] Author, "Title", Journal, Year
    """
    # Implementation
    pass
```

### Function Design Principles

1. **Single Responsibility**: Each function should do one thing well
2. **Clear Naming**: Function names should clearly indicate their purpose
3. **Input Validation**: Validate inputs and provide helpful error messages
4. **Type Hints**: Use type hints where appropriate (Python 3.6+)

```python
from typing import Union, List
import numpy as np

def matround(matrix: np.ndarray, 
             dec: Union[int, None] = None, 
             sf: Union[int, None] = None) -> np.ndarray:
    """Round matrix to specified precision."""
    # Implementation
    pass
```

---

## Testing Guidelines

### Writing Tests

All new functions should include unit tests:

```python
import pytest
import numpy as np
from geomatics import matround

def test_matround_decimal_places():
    """Test matrix rounding to decimal places."""
    matrix = np.array([[1.23456, 2.34567]])
    result = matround(matrix, dec=3)
    expected = np.array([[1.235, 2.346]])
    np.testing.assert_array_almost_equal(result, expected)

def test_matround_significant_figures():
    """Test matrix rounding to significant figures."""
    matrix = np.array([[123.456, 234.567]])
    result = matround(matrix, sf=4)
    expected = np.array([[123.5, 234.6]])
    np.testing.assert_array_almost_equal(result, expected, decimal=1)
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=geomatics

# Run specific test file
pytest tests/test_matrix.py
```

### Test Coverage

- Aim for at least 80% code coverage
- Test edge cases and error conditions
- Test with various input types (lists, arrays, scalars)

---

## Submitting Changes

### Pull Request Process

1. **Update Documentation**
   - Add/update docstrings for new functions
   - Update README.md if adding major features
   - Add examples to demonstrate new functionality

2. **Write Tests**
   - Add unit tests for new functions
   - Ensure all tests pass
   - Check test coverage

3. **Follow Commit Conventions**
   ```
   type(scope): brief description
   
   Longer description if needed
   
   Fixes #issue_number
   ```
   
   Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
   
   Examples:
   - `feat(coordinates): add UTM to geographic conversion`
   - `fix(matround): handle negative numbers correctly`
   - `docs(readme): add installation troubleshooting`

4. **Create Pull Request**
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe the changes and their purpose
   - Include example usage if applicable
   - Add "Fixes #issue_number" if closing an issue

5. **Code Review Process**
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Keep discussion focused and professional
   - Once approved, maintainers will merge

### PR Checklist

Before submitting your PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All new functions have docstrings
- [ ] Unit tests added for new functionality
- [ ] All tests pass
- [ ] Documentation updated (README, examples)
- [ ] Commit messages follow conventions
- [ ] Branch is up-to-date with main

---

## Development Roadmap

### Short-term Goals (v1.1)
- [ ] Add UTM coordinate transformations
- [ ] Implement geodetic distance calculations
- [ ] Add more statistical tests (chi-square, F-test)
- [ ] Improve error handling and validation

### Medium-term Goals (v1.2)
- [ ] Web Mercator projection utilities
- [ ] Datum transformation functions
- [ ] Height system conversions
- [ ] Extended documentation with tutorials

### Long-term Goals (v2.0)
- [ ] Integration with GeoPandas
- [ ] Support for more coordinate systems
- [ ] GUI for common calculations
- [ ] Package optimization for large datasets

---

## Questions?

If you have questions about contributing:

1. Check existing issues and pull requests
2. Review this contributing guide
3. Contact the maintainer:
   - GitHub: [@mikemost](https://github.com/mikemost)
   - LinkedIn: [Michael Mutale](https://www.linkedin.com/in/mkmutale/)

---

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to the Geomatics package! Your efforts help improve geomatics education and research worldwide. 🌍

---

*This contributing guide is adapted from open source best practices and tailored for the geomatics engineering community.*
