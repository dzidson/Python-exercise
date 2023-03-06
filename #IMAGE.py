#IMAGE


from PIL import Image

im = Image.open("zdj.jpg")

print(im.height, im.width, im.size, im.mode, im.format)

im.show("PYTHON")