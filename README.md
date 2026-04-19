# Geomatics

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

A Python library providing utilities for geomatics engineering numerical methods, coordinate transformations, and surveying calculations.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Use Cases](#use-cases)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## 🌍 Overview

The **geomatics** package is designed specifically for geomatics engineering students, professionals, and researchers. It provides a comprehensive set of tools for performing numerical computations commonly required in surveying, geodesy, photogrammetry, and spatial analysis.

This library was developed to support teaching and research at the **Geomatics Engineering Department, Copperbelt University**, and is used in courses including:
- GE 410: Numerical Methods for Geomatics
- GE 422: Digital Photogrammetry
- GE 550: Advanced Topics in Geomatics

---

## ✨ Features

### 🔢 **Numerical Utilities**
- **Matrix rounding** with configurable precision (significant figures or decimal places)
- **Significant figure rounding** for precise scientific calculations
- Clean display of numerical results for reports and documentation

### 🌐 **Coordinate System Utilities**
- **Decimal degrees to DMS (Degrees, Minutes, Seconds)** conversion
- Coordinate transformation support
- Geodetic calculations

### 📊 **Statistical Analysis**
- **Pope's Tau Test** for outlier detection in observations
- Error propagation calculations
- Quality control for surveying measurements

### 🧮 **Symbolic Mathematics Integration**
- Seamless integration with **SymPy** for symbolic computations
- Support for analytical derivations in adjustment computations
- Matrix operations for least squares adjustments

---

## 🚀 Installation

### Option 1: Install from GitHub (Recommended)

```bash
pip install git+https://github.com/mikemost/geomatics.git
```

### Option 2: Clone and Install Locally

```bash
# Clone the repository
git clone https://github.com/mikemost/geomatics.git

# Navigate to the directory
cd geomatics

# Install in development mode
pip install -e .
```

### Option 3: Direct Download

1. Download the repository as a ZIP file
2. Extract to your local machine
3. Navigate to the extracted folder
4. Run: `pip install -e .`

### Verify Installation

```python
import geomatics
print("Geomatics package installed successfully!")
```

---

## 🎯 Quick Start

### Example 1: Matrix Rounding

```python
from geomatics import matround
import numpy as np

# Create a matrix with high precision values
matrix = np.array([
    [1.23456789, 2.34567890],
    [3.45678901, 4.56789012]
])

# Round to 3 decimal places
rounded = matround(matrix, dec=3)
display(rounded)
# Output:
# [[1.235 2.346]
#  [3.457 4.568]]

# Round to 4 significant figures
rounded_sf = matround(matrix, sf=4)
display(rounded_sf)
```

### Example 2: Degree to DMS Conversion

```python
from geomatics import degtodms

# Convert decimal degrees to DMS format
angle_dd = 115.6650  # degrees
angle_dms = degtodms(angle_dd)
print(angle_dms)
# Output: "115° 39' 54""
```

### Example 3: Significant Figure Rounding

```python
from geomatics import roundsf

# Round to 5 significant figures
value = 123456.789
rounded_value = roundsf(value, sig=5)
print(rounded_value)
# Output: 123460.0
```

### Example 4: Outlier Detection with Pope's Tau Test

```python
from geomatics import tau, roundsf
import numpy as np

std_residuals = np.array([0.5, 1.2, -0.8, 3.5, 0.3, -1.1, 0.9])
n_obs = len(std_residuals)
df = 4  # Degrees of freedom

# Get critical value
critical_value = tau(0.05, n_obs, df)

print(f"Testing {n_obs} observations")
print(f"Critical Tau value: {roundsf(critical_value, 3)}")
print("\nOutlier Analysis:")

for i, residual in enumerate(std_residuals, 1):
    abs_residual = abs(residual)
    status = "OUTLIER" if abs_residual > critical_value else "OK"
    print(f"Obs {i}: {roundsf(residual, 2):6.2f} - {status}")
```

---

## 📖 Documentation

### Core Functions

#### `matround(matrix, dec=None, sf=None)`

Rounds a matrix to specified decimal places or significant figures.

**Parameters:**
- `matrix` (array-like): Input matrix or array
- `dec` (int, optional): Number of decimal places
- `sf` (int, optional): Number of significant figures

**Returns:**
- Rounded matrix/array

**Note:** Specify either `dec` OR `sf`, not both.

---

#### `degtodms(degrees)`

Converts decimal degrees to Degrees, Minutes, Seconds format.

**Parameters:**
- `degrees` (float): Angle in decimal degrees

**Returns:**
- String in format "D° M' S""

**Example:**
```python
angle = 45.508333  # 45° 30' 30"
dms = degtodms(angle)
# Returns: "45° 30' 30""
```

---

#### `roundsf(value, n=5)`

Rounds a value to specified significant figures.

**Parameters:**
- `value` (float): Number to round
- `n` (int): Number of significant figures (default: 5)

**Returns:**
- Rounded value

**Example:**
```python
# Round to 3 significant figures
result = roundsf(12345.6789, 3)
# Returns: 12300.0
```

---

#### `tau(alpha, n_obs, df=0.05)`

Performs Pope's Tau test for outlier detection in observations.

**Parameters:**
- `alpha` (float): Confidence level (default: 0.05)
- `n_obs ` (int): Number of observations in the network
- `df ` (int): Degrees of freedom (number of observations minus number of unknowns)

**Returns:**
- float representing the critical Tau value

**Application:** Used in least squares adjustment and quality control of surveying measurements.

---

## 💼 Use Cases

### Academic Applications

1. **GE 410 - Numerical Methods for Geomatics**
   - Matrix computations in least squares adjustment
   - Error propagation calculations
   - Displaying results with appropriate precision

2. **GE 422 - Digital Photogrammetry**
   - Coordinate transformations
   - Bundle adjustment computations
   - Quality assessment of photogrammetric solutions

3. **GE 500 - Final Year Projects**
   - Data processing and analysis
   - Research computations
   - Professional report generation

### Professional Applications

- **Surveying Data Processing**: Clean formatting of coordinates and measurements
- **Geodetic Computations**: Coordinate transformations and datum conversions
- **Quality Control**: Outlier detection in measurement series
- **Research**: Standardized numerical output for publications

### Integration with Other Tools

```python
# Example: Integration with least squares adjustment
from geomatics import matround, degtodms, pope_tau_test
import numpy as np

# After performing adjustment
adjusted_coords = np.array([[5581.73456, 7751.47634],
                           [6634.09812, 6823.27845]])

# Display with 3 decimal places
print("Adjusted Coordinates:")
print(matround(adjusted_coords, dec=3))

# Convert azimuths to DMS
azimuth = 115.6650
print(f"Azimuth: {degtodms(azimuth)}")

```

---

## 📦 Dependencies

The geomatics package requires:

- **Python 3.6+**
- **numpy**: Numerical computations
- **sympy**: Symbolic mathematics (automatically installed)

To manually install dependencies:
```bash
pip install numpy sympy
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/NewFeature`)
3. **Commit** your changes (`git commit -m 'Add NewFeature'`)
4. **Push** to the branch (`git push origin feature/NewFeature`)
5. **Open** a Pull Request

### Areas for Contribution

- Additional coordinate transformation functions
- More statistical tests for quality control
- Datum transformation utilities
- Documentation improvements
- Bug fixes and performance optimizations

---

## 👨‍🏫 Author

**Michael Mutale, MSc**

- **Position**: Lecturer II, Geomatics Engineering Department
- **Institution**: Copperbelt University, School of Mines and Mineral Sciences
- **Specialization**: Photogrammetry & Geoinformatics
- **Experience**: 20+ years in GIS, Remote Sensing, and Spatial Analysis

**Connect:**
- 🔗 [LinkedIn](https://www.linkedin.com/in/mkmutale/)
- 🐦 [Twitter](https://twitter.com/mkmutale)
- 🌐 [Website](http://mkmthunderbird.com)
- 📧 [ORCID](https://orcid.org/0009-0008-0501-6550)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Citation

If you use this package in academic work, please cite:

```
Mutale, M. (2024). Geomatics: A Python Library for Geomatics Engineering Numerical Methods. 
Copperbelt University, Kitwe, Zambia.
Available at: https://github.com/mikemost/geomatics
```

---

## 🔄 Changelog

### Version 1.0.0 (Current)
- Initial release
- Core functions: matround, degtodms, sigfig, pope_tau_test
- Integration with SymPy
- Comprehensive documentation

### Planned Features
- [ ] Additional coordinate transformation functions
- [ ] Web Mercator projection utilities
- [ ] UTM zone calculations
- [ ] Geodetic distance computations
- [ ] More statistical tests for surveying data

---

## 📞 Support

### Issues and Bug Reports

If you encounter any issues or bugs, please [open an issue](https://github.com/mikemost/geomatics/issues) on GitHub with:
- A clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your Python version and operating system

### Questions and Help

For questions about usage:
- Check the [documentation](#documentation) above
- Review the [examples](#quick-start)
- Contact the author via [LinkedIn](https://www.linkedin.com/in/mkmutale/)

### Educational Use

Students at Copperbelt University can contact me directly through:
- Office hours in the Geomatics Engineering Department
- University email
- Course management systems

---

## 🌟 Acknowledgments

- **Copperbelt University** - For supporting the development of educational tools
- **Students of GE 410** - For testing and providing feedback
- **Open Source Community** - For the excellent tools this package builds upon

---

## 📚 Related Projects

- [PyProj](https://github.com/pyproj4/pyproj) - Python interface to PROJ for coordinate transformations
- [GeoPandas](https://geopandas.org/) - Geospatial data analysis
- [Rasterio](https://rasterio.readthedocs.io/) - Raster data processing
- [GDAL/OGR](https://gdal.org/) - Geospatial data abstraction library

---

<div align="center">

**Made with ❤️ for the Geomatics Engineering Community**

[⬆ Back to Top](#geomatics)

</div>
