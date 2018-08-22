import math
from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()
w = img.width
h = img.height

for i in range(0, w):
    for j in range(0, h):
        if j == math.ceil(math.tan(h/w)*i):
            pixels[i,j] = 255,255,255

print('end')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(fotoDIAGONAL).jpg")

