# codes2

A small Python utilities package for basic image operations (grayscale, resize, format conversion).

This repository modernizes a very small script that converted an image into grayscale — it adds:

- A small, testable Python package `image_tool` under `src/`.
- A tiny CLI (`image-tool`) via `image_tool.cli`.
- Unit tests using `pytest`.
- GitHub Actions CI to run tests on push and PRs.

## Install

Clone repository and install using pip:

```bash
python -m pip install -e .
```

Install requirements for development and testing:

```bash
python -m pip install -r requirements.txt
```

## CLI Examples

Convert a single image to grayscale:

```bash
python -m image_tool.cli grayscale path/to/input.jpg --output path/to/out.jpg
```

Resize an image:

```bash
python -m image_tool.cli resize path/to/input.jpg 800 600 --output path/to/resized.jpg
```

Change image format:

```bash
python -m image_tool.cli convert path/to/input.png jpeg
```

## Contribution ideas

- Add additional transformations (rotate, crop) and preserve EXIF metadata.
- Add batch processing for directories.
- Add type hints and mypy checks.

## License

This project uses the MIT license — see `LICENSE` file for details.
