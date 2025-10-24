# Geomatics Package

This Python package provides utilities for geomatics engineering numerical methods.

## Installation

Once the package is installed you can use it as follows:

```python
# Import the whole package
import geomatics

# Or import specific functions
from geomatics import round_matrix, degtodms, roundsf, tau
```

## Available Functions

- `round_matrix(matrix, digits, method='sig')`: Round each element of a Sympy matrix
  - `method='sig'` or `'significant'`: Round to significant figures
  - `method='dec'` or `'decimal'`: Round to decimal places

- `degtodms(decimal, decimals=0)`: Convert decimal degrees to degrees-minutes-seconds format

- `roundsf(value, n)` : Rounds a value to a given number of significant figures

- `tau(alpha: float, n_obs: int, df: int)` : Get Pope's Tau critical value for outlier detection in geodetic networks.
