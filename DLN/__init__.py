"""
DLN means "DLN Lightweight Notation".

This module provides functions to work with the DLN image format, a lightweight image format designed for efficient storage and transmission.

For more information, visit the [DLN GitHub Repository](https://github.com/shp0717/DLN), or run `DLN.tutorial()`.
"""

from DLN.__main__ import dump, dumps, load, loads  # , autoconvert
from PIL import Image


def tutorial():
    """
    Show tutorial information about the DLN module.
    """
    print(
        """
    DLN Tutorial
    -------------
    1. To convert an image to DLN format:
       DLN.dump('image.png', open('image.dln', 'wb'))
    2. To load an image from DLN format:
       image = DLN.load(open('image.dln', 'rb'))
    3. For more information, visit the DLN GitHub Repository:
       https://github.com/shp0717/DLN
    """
    )


__all__ = [
    "dump",
    "dumps",
    "load",
    "loads",
    "tutorial",
    "Image",
]


if __name__ == "__main__":
    tutorial()
