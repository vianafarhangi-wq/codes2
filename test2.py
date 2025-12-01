"""A tiny demo that shows how to use the image_tool package.

This keeps backwards compatibility with the earlier `test2.py` script but uses
the new package implementation.
"""
from pathlib import Path
import sys

from image_tool.convert import to_grayscale


def main(argv=None):
	argv = argv if argv is not None else sys.argv[1:]
	if not argv:
		print("Usage: python test2.py <input-image> [output-image]")
		return 1
	input_path = Path(argv[0])
	out = Path(argv[1]) if len(argv) > 1 else None
	output = to_grayscale(input_path, out)
	print(f"Saved grayscale image to: {output}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
