from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        
        r, g, b = pixels[i, j]
        
        avg = ((r + g + b)/3)
        if avg <= 125:
            r = 0
            g = 0
            b = 0
        else:
            r = 255
            g = 255
            b = 255

        pixels[i, j] = (r, g, b)

print('end')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto2).jpg")
