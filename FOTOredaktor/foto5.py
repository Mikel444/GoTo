from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()
w = img.width
h = img.height

for i in range(0, w//2):
    for j in range(0, h):
        pixels[w-i-1, j] = pixels[i, j]

print('end1')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto5_1).jpg")

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()
w = img.width
h = img.height

for i in range(0, w):
    for j in range(0, h//2):
        pixels[i, h-j-1] = pixels[i, j]

print('end2')
img.show()
img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto5_2).jpg")
