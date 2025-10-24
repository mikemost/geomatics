from setuptools import setup, find_packages

setup(
    name="geomatics",
    version="1.0.5",
    packages=find_packages(),
    install_requires=[
        "sympy",
        "numpy",
        "matplotlib"
    ],
    author="Michael Mutale",
    author_email="mikemost@gmail.com",
    description="A package for geomatics engineering calculations and utilities",
    keywords="geomatics, surveying, engineering",
    url="https://github.com/mikemost/geomatics",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
