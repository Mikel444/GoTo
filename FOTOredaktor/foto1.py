from PIL import Image

img = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg")

pixels = img.load()
print("start")
for i in range(img.width):
    for j in range(img.height):
        
        r, g, b = pixels[i, j]

        avg = int((r + g + b) / 3)

        pixels[i, j] = (avg, avg, avg)
print("end")
img.show()

img.save("/home/goto/Desktop/goto Misha 2018/SportCar(foto1).jpg")
