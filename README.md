# Geomatics Package

This Python package provides utilities for geomatics engineering numerical methods.

## Installation

This package is installed in development mode. To use it:

```python
# Import the whole package
import geomatics

# Or import specific functions
from geomatics import round_matrix, degtodms
```

## Available Functions

- `round_matrix(matrix, digits, method='sig')`: Round each element of a Sympy matrix
  - `method='sig'` or `'significant'`: Round to significant figures
  - `method='dec'` or `'decimal'`: Round to decimal places

- `degtodms(decimal, decimals=0)`: Convert decimal degrees to degrees-minutes-seconds format

## Updating Notebooks

All notebooks in the GE 410 Numerical Methods for Geomatics workspace have been updated to use this package instead of the original `myfunctions.py` module.

To update additional notebooks, run:

```
python update_imports.py
```

This will scan all Jupyter notebooks in the workspace and replace:
- `from myfunctions import ...` with `from geomatics import ...`
- `import myfunctions` with `import geomatics`
