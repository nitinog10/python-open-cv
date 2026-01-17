
from PIL import Image

img = Image.open("./Image.jpg")
gi = img.convert("L")       # L => low level of image
gi.show()
img.show()
