from PIL import Image
import random

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')

pixels = img.load()

plus = 125

for i in range(img.width):
    for j in range(img.height):
        h = random.randint(-plus,plus)
        r, g, b = pixels[i, j]
        
        r = r + h
        if r >= 255:
            r = 255
        if r < 0:
            r = 0
            
        g = g + h
        if g >= 255:
            g = 255
        if g < 0:
            g = 0
            
        b = b + h
        if b >= 255:
            b = 255
        if b < 0:
            b = 0

        pixels[i, j] = (r, g, b)

print('end')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto3).jpg")

