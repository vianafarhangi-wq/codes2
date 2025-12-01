"""Image conversion and processing utilities.

Provides simple, testable functions for common conversions as used in the
original `test2.py` script.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

from PIL import Image


def to_grayscale(in_path: Path | str, out_path: Optional[Path | str] = None) -> Path:
    """Convert an image to grayscale and save it.

    Args:
        in_path: Path to input image.
        out_path: Optional path for output image. If None, adds `_gray` suffix.
    Returns:
        Path to the saved output image.
    """
    in_path = Path(in_path)
    if out_path is None:
        out_path = in_path.with_name(in_path.stem + "_gray" + in_path.suffix)
    out_path = Path(out_path)

    with Image.open(in_path) as im:
        gray = im.convert("L")
        # If user requests an RGB output, convert back, but keep 'L' by default
        gray.save(out_path)
    return out_path


def resize_image(in_path: Path | str, out_path: Optional[Path | str] = None,
                 size: Tuple[int, int] = (800, 600)) -> Path:
    """Resize an image to the requested size (width, height).

    Args:
        in_path: Path to input image.
        out_path: Optional path for output image. If None, adds `_resized` suffix.
        size: (width, height) tuple.
    Returns:
        Path to the saved output image.
    """
    in_path = Path(in_path)
    if out_path is None:
        out_path = in_path.with_name(in_path.stem + f"_resized_{size[0]}x{size[1]}" + in_path.suffix)
    out_path = Path(out_path)

    with Image.open(in_path) as im:
        resized = im.resize(size)
        resized.save(out_path)
    return out_path


def convert_format(in_path: Path | str, out_format: str, out_path: Optional[Path | str] = None) -> Path:
    """Convert image format (e.g., PNG to JPEG).

    Args:
        in_path: Path to input image.
        out_format: Format string recognized by Pillow (JPEG, PNG, etc.).
        out_path: Optional path for output image. If None, change suffix to out_format.
    Returns:
        Path to the saved output image.
    """
    in_path = Path(in_path)
    fmt = out_format.lower()
    if out_path is None:
        suffix = "." + fmt
        out_path = in_path.with_suffix(suffix)
    out_path = Path(out_path)

    with Image.open(in_path) as im:
        # Pillow expects format names such as "JPEG" rather than "jpg"
        im.save(out_path, format=out_format.upper())
    return out_path
