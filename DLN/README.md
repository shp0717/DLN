# DLN - A Lightweight Image Format
DLN is a lightweight image format designed for efficient storage and transmission.

## Overview

DLN builds on existing image formats, using modern compression to shrink file size while preserving quality.

## Features

- Lightweight and efficient image format

- Supports lossless compression

- Easy to use with existing Python image libraries

## What Kinds of Image Formats Does DLN Support?

DLN is designed to work with a variety of image formats, including:

- `PNG`

- `JPEG`

And it supports these styles of images:

- `Black and White`

- `Grayscale`

- `RGB`

- `RGBA`

- `CMYK`

- `YCbCr`

- And More!

## What Are the Benefits of Using DLN?

1. **Reduced File Size**: DLN uses advanced compression techniques to minimize file size without sacrificing quality.

2. **Fast Loading Times**: The format is optimized for quick loading, making it ideal for web and mobile applications.

3. **Compatibility**: DLN is designed to work seamlessly with popular Python image libraries, ensuring easy integration into existing workflows.

## Why Does The DLN File Size So Important?

In today's digital landscape, file size is a critical factor for performance, especially for web and mobile applications. Smaller file sizes lead to faster loading times, reduced bandwidth usage, and improved user experiences. DLN's efficient compression techniques help achieve these goals.

## How Does It Work?

DLN uses a combination of advanced compression algorithms and image optimization techniques to reduce file size while maintaining quality. By analyzing image content and applying the most effective compression methods, DLN ensures that images are as small as possible without noticeable loss of detail.

## What Are The Technical Details?

- DLN just uses 5 bytes for the Magic, Version, and Image Style fields.

- Taking RGBA format as an example, the image data is stored in a compressed format, with each pixel just using less than 4 bytes.

- We tested the encoding system by encoding a 1024x1024 transparent image and found that the PNG file requires more than 21KB of storage space, while the DLN format file just uses 65 bytes.

## What Does DLN Mean?

DLN has two meanings:

1. **DLN Lightweight Notation** - Refers to the format's lightweight and efficient nature.

2. **DLN Loads Nicely** - Emphasizes the format's ability to load images quickly and easily.

## Python Version

DLN requires Python 3.6 or higher.

## Used PyPI Packages

- `pillow`

- `zstandard`

## Used Built-in Modules

- `pickle`

- `io`

## Methods

- `DLN.dumps(image: PIL.Image.Image) -> bytes`: Serialize an image to DLN format.

- `DLN.dump(image: PIL.Image.Image, file: io.BufferedWriter) -> None`: Serialize an image to DLN format and write it to a file.

- `DLN.loads(data: bytes) -> PIL.Image.Image`: Deserialize a DLN format image.

- `DLN.load(file: io.BufferedReader) -> PIL.Image.Image`: Deserialize a DLN format image from a file.

## Installation

You can install DLN using pip:

``` bash
pip install dln
```

## Examples

``` python
import DLN

# Load an image
image = DLN.Image.open("example.png") # DLN.Image = PIL.Image

# Serialize the image to DLN format
dln_data = DLN.dumps(image)

# Deserialize the DLN format image
image2 = DLN.loads(dln_data)

# Save the DLN format image to a file
with open("example.dln", "wb") as f:
    DLN.dump(image, f)

# Load the DLN format image from a file
with open("example.dln", "rb") as f:
    image3 = DLN.load(f)

# Show the images
image.show()
image2.show()
image3.show()

# Save the PNG format image to a file
image.save("example.png")
```

## Warning

1. DLN is still in development and may not be suitable for production use. Use at your own risk.

2. We cannot guarantee lossless image compression or support for all file formats.

3. It uses the `pickle` module, which may execute any malicious code when loading, so please **do not** casually open files from unknown sources. [More Info](https://docs.python.org/3/library/pickle.html#security-concerns)

4. If you encounter any problems, please report them at [DLN GitHub Repository](https://github.com/shp0717/DLN) or send an email to dylanjangkuma@gmail.com

5. Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
