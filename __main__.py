__FORMAT__ = """
DLN Image Format:
<magic>: 3 byte, ascii, "DLN"
<width>: 1+ byte, hex
<zip-count>: 1 byte, binary (00 ~ 2F)
<height>: 1+ byte, hex
<mode>: 1 byte, binary (00 ~ 0B)
<meta-length>: 1+ byte, hex
<VER>: 1 byte, binary (00 ~ FF)
<meta>: 1+ byte, binary (00 ~ FF)
<pixels>: 1+ byte, binary (00 ~ FF)
"""

from PIL import Image
from io import BufferedReader, BufferedWriter
import zstandard as zstd
import pickle

version = b"\x01"
"""
Version 0.1
"""
version_text = __version__ = f"{version[0] // 16}.{version[0] % 16}"
"""
Version 0.1
"""
magic = b"DLN"
modes = [
    "1",  # 1-bit pixels, black and white, stored with one pixel per byte
    "L",  # 8-bit pixels, grayscale
    "P",  # 8-bit pixels, mapped to any other mode using a color palette
    "RGB",  # 3x8-bit pixels, true color
    "RGBA",  # 4x8-bit pixels, true color with transparency mask
    "CMYK",  # 4x8-bit pixels, color separation
    "I",  # 32-bit signed integer pixels
    "F",  # 32-bit floating point pixels
    "LA",  # L with alpha
    "RGBX",  # true color with padding
    "YCbCr",  # color video format
    "I;16",  # 16-bit unsigned integer pixels
]
mode_length = {
    "1": 1,  # 1-bit pixels, stored as 1 byte per pixel here
    "L": 1,  # 8-bit grayscale
    "P": 1,  # 8-bit palette
    "RGB": 3,  # 3 bytes per pixel
    "RGBA": 4,  # 4 bytes per pixel (with alpha)
    "CMYK": 4,  # 4 bytes per pixel
    "I": 4,  # 32-bit signed integer pixels
    "F": 4,  # 32-bit floating point pixels
    "LA": 2,  # L with alpha
    "RGBX": 4,  # RGB with padding
    "YCbCr": 3,  # Color video format
    "I;16": 2,  # 16-bit unsigned integer pixels
}


class DLNImageDecodeError(Exception):
    pass


def bytes_format(*args: list[bytes]) -> bytes:
    return b"".join([i for i in args])


def dumps(image: Image.Image) -> bytes:
    """
    Convert a PIL Image to a binary DLN format.
    """
    mode = modes.index(image.mode)
    meta = pickle.dumps(image.info)
    size = [hex(i)[2:].encode() for i in image.size]
    pixels = image.tobytes()
    meta_zip_count, pixels_zip_count = 0, 0
    for _ in range(1, 3):
        if len(zstd.compress(meta)) / len(meta) < 1:
            meta = zstd.compress(meta)
            meta_zip_count += 1
        else:
            break
    for _ in range(1, 16):
        if len(zstd.compress(pixels)) / len(pixels) < 1:
            pixels = zstd.compress(pixels)
            pixels_zip_count += 1
        else:
            break
    meta_length = hex(len(meta))[2:].encode()
    zip_count = bytes([meta_zip_count * 16 + pixels_zip_count])
    imgdata = bytes_format(magic, size[0], zip_count, size[1], bytes([mode]), meta_length, version, meta, pixels)
    return imgdata


def dump(image: Image.Image, file: BufferedWriter):
    """
    Convert a PIL Image to a binary DLN file,
    then write in a binary file.

    Example:
    ```python
    from PIL import Image
    import DLN

    with open("image.dln", "wb") as f:
        DLN.dump(Image.open("image.png"), f)  # Save the image in DLN format
    ```
    """
    file.write(dumps(image))


def loads(image_data: bytes) -> Image.Image:
    """
    Load image from a binary DLN file data.
    """
    data = image_data
    magic_name, data = data[:3], data[3:]
    if magic_name != magic:
        raise DLNImageDecodeError("Invalid DLN file format")
    width = b""
    height = b""
    for i, j in enumerate(data):
        if j not in tuple(b"0123456789abcdef"):
            break
        width += bytes([j])
    zip_count, data = data[i], data[i + 1 :]
    for i, j in enumerate(data):
        if j not in tuple(b"0123456789abcdef"):
            break
        height += bytes([j])
    width, height = int(width.decode(), 16), int(height.decode(), 16)
    data = data[i:]
    mode, data = data[0], data[1:]
    mode = modes[mode]
    meta_length = b""
    for i, j in enumerate(data):
        if j not in tuple(b"0123456789abcdef"):
            break
        meta_length += bytes([j])
    meta_length = int(meta_length.decode(), 16)
    ver, data = data[i], data[i + 1 :]
    ver = bytes([ver])
    ver_text = f"{ver[0] // 16}.{ver[0] % 16}"
    if ver != version:
        raise DLNImageDecodeError(f"Invalid DLN file version, should be '{version_text}', but got '{ver_text}'.")
    meta = data[:meta_length]
    pixels = data[meta_length:]
    if isinstance(meta, int):
        meta = bytes([meta])
    if isinstance(pixels, int):
        pixels = bytes([pixels])
    meta_zip_count, pixels_zip_count = zip_count // 16, zip_count % 16
    for _ in range(meta_zip_count):
        meta = zstd.decompress(meta)
    for _ in range(pixels_zip_count):
        pixels = zstd.decompress(pixels)
    image = Image.frombytes(mode, (width, height), pixels)
    image.info = pickle.loads(meta)
    return image


def load(file: BufferedReader) -> Image.Image:
    """
    Load image from a binary DLN file.

    Example:
    ``` python
    with open("image.dln", "rb") as f:
        image = DLN.load(f)  # Load the image from DLN format
        image.show()         # Show the loaded image
    ```
    """
    return loads(file.read())
