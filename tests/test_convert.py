import tempfile
from pathlib import Path

from PIL import Image

from image_tool.convert import to_grayscale, resize_image, convert_format


def create_temp_image(tmp_path: Path, size=(10, 10), color=(255, 0, 0)) -> Path:
    p = tmp_path / "test_rgb.png"
    img = Image.new("RGB", size, color=color)
    img.save(p)
    return p


def test_to_grayscale(tmp_path: Path):
    p = create_temp_image(tmp_path)
    out = to_grayscale(p)
    assert out.exists()
    with Image.open(out) as im:
        assert im.mode == "L"


def test_resize(tmp_path: Path):
    p = create_temp_image(tmp_path, size=(50, 20))
    out = resize_image(p, size=(20, 10))
    assert out.exists()
    with Image.open(out) as im:
        assert im.size == (20, 10)


def test_convert_format(tmp_path: Path):
    p = create_temp_image(tmp_path)
    out = convert_format(p, "JPEG")
    assert out.exists()
    assert out.suffix.lower() == ".jpeg" or out.suffix.lower() == ".jpg"


def test_cli_grayscale(tmp_path: Path):
    # Test CLI grayscale command by calling main with args
    from image_tool import cli

    p = create_temp_image(tmp_path)
    output = tmp_path / "cli_gray.png"
    rc = cli.main(["grayscale", str(p), "--output", str(output)])
    assert rc == 0
    assert output.exists()
    from PIL import Image
    with Image.open(output) as im:
        assert im.mode == "L"
