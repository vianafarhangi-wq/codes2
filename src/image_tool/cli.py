"""Command-line interface for image_tool.

Intentionally simple and dependency-free: it uses argparse so the package remains
lightweight for a minimal example repository contribution.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .convert import to_grayscale, resize_image, convert_format


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="image-tool", description="Small image utilities CLI.")
    subparsers = parser.add_subparsers(dest="command")

    p_gray = subparsers.add_parser("grayscale", help="Convert an image to grayscale")
    p_gray.add_argument("input", help="Input image path")
    p_gray.add_argument("--output", "-o", help="Output path (optional)")

    p_resize = subparsers.add_parser("resize", help="Resize an image")
    p_resize.add_argument("input", help="Input image path")
    p_resize.add_argument("width", type=int, help="Target width")
    p_resize.add_argument("height", type=int, help="Target height")
    p_resize.add_argument("--output", "-o", help="Output path (optional)")

    p_fmt = subparsers.add_parser("convert", help="Convert image format")
    p_fmt.add_argument("input", help="Input image path")
    p_fmt.add_argument("format", help="Target format (e.g., JPEG, PNG)")
    p_fmt.add_argument("--output", "-o", help="Output path (optional)")

    args = parser.parse_args(argv)
    if args.command == "grayscale":
        out = to_grayscale(args.input, args.output)
        print(f"Saved grayscale image: {out}")
    elif args.command == "resize":
        out = resize_image(args.input, args.output, size=(args.width, args.height))
        print(f"Saved resized image: {out}")
    elif args.command == "convert":
        out = convert_format(args.input, args.format, args.output)
        print(f"Saved converted image: {out}")
    else:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
