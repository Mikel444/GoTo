from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")
print('start')
pixels = img.load()

w = img.width
h = img.height

for i in range(0, w//2):
    for j in range(0, h//2):
        
        r, g, b = pixels[i, j]
        pixels[i, j] = (r, g, b)
        
for i in range(w//2,w):
    for j in range(0,h//2):
        
        r, g, b = pixels[i, j]
        pixels[i, j] = (200, g, b)
        
for i in range(0, w//2):
    for j in range(h//2,h):
        
        r, g, b = pixels[i, j]
        pixels[i, j] = (r, 200, b)
        
for i in range(w//2,w):
    for j in range(h//2,h):
        
        r, g, b = pixels[i, j]
        pixels[i, j] = (r, g, 200)

print('end')
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto4).jpg")

