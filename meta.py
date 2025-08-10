from DLN.__main__ import version_text

__author__ = "Dylan Jang"

__used_pypi_packages__ = [
    "pillow",
    "zstandard",
]

__used_modules__ = [
    "pickle",
    "io",
]

__package__ = "DLN"

__doc__ = """
DLN means "DLN Lightweight Net-Pictures".

This module provides functions to work with the DLN image format, a lightweight image format designed for efficient storage and transmission.

For more information, visit the [DLN GitHub Repository](https://github.com/shp0717/DLN).
"""

__email__ = "dylanjangkuma@gmail.com"

__python_version__ = ">=3.6"

__git__ = "https://github.com/shp0717/DLN"

__version__ = version_text + ".0"

__readme__ = open("README.md").read()

__meta__ = """
Author: Dylan Jang
Used PyPI Packages: pillow, zstandard
Used Modules: pickle, io
Package: DLN
Email: dylanjangkuma@gmail.com
Python Version: >=3.6
Git: https://github.com/shp0717/DLN
Version: 0.1.0
"""
