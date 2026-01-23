"""
Setup script for the geomatics package
"""

from setuptools import setup, find_packages
import pathlib

# Read the contents of README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='geomatics',
    version='1.0.0',
    
    # Description
    description='Python utilities for geomatics engineering numerical methods',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    # Author details
    author='Michael Mutale',
    author_email='',  # Add your email if you want
    
    # URLs
    url='https://github.com/mikemost/geomatics',
    project_urls={
        'Bug Reports': 'https://github.com/mikemost/geomatics/issues',
        'Source': 'https://github.com/mikemost/geomatics',
        'Documentation': 'https://github.com/mikemost/geomatics#readme',
    },
    
    # License
    license='MIT',
    
    # Classifiers help users find your project
    classifiers=[
        # Development status
        'Development Status :: 4 - Beta',
        
        # Intended audience
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        
        # Topic
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        
        # License
        'License :: OSI Approved :: MIT License',
        
        # Python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        
        # Operating systems
        'Operating System :: OS Independent',
    ],
    
    # Keywords
    keywords='geomatics, surveying, geodesy, gis, photogrammetry, coordinate-transformation, numerical-methods',
    
    # Package discovery
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    
    # Python version requirement
    python_requires='>=3.6',
    
    # Dependencies
    install_requires=[
        'numpy>=1.19.0',
        'sympy>=1.6',
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.12',
            'black>=21.0',
            'flake8>=3.9',
        ],
        'docs': [
            'sphinx>=4.0',
            'sphinx-rtd-theme>=0.5',
        ],
    },
    
    # Entry points (if you want to create command-line scripts)
    # entry_points={
    #     'console_scripts': [
    #         'geomatics=geomatics.cli:main',
    #     ],
    # },
    
    # Include additional files
    include_package_data=True,
    
    # Zip safe
    zip_safe=False,
)
