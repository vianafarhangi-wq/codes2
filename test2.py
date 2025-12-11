#رنگ تصویر

from PIL import Image
image = Image.open("tuf.jpg.jpg")
grayImage = image.convert("L")
grayImage = image.convert("L")
grayImage.save("newname.jpg")
