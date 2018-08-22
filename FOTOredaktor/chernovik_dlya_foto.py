from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        
        r, g, b = pixels[i, j]




        pixels[i, j] = (r, g, b)

print('end')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto).jpg")

