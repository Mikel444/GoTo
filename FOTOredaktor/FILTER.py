
from PIL import Image, ImageDraw 

image = Image.open("/home/goto/Desktop/goto Misha 2018/SportCar(starter).jpg") 
draw = ImageDraw.Draw(image) 
w = image.size[0] 
h = image.size[1]  	
pixels = image.load()

print('start')
k = 3 #float(input("Введите коэфициент от 1 до 3: "))
for i in range(image.width):
    for j in range(image.height):
        a = pixels[i, j] [0]
        b = pixels[i, j] [1]
        c = pixels[i, j] [2]
        draw.point((i, j), (a+int(30*k), b+int(21*k), c+int(27*k))) 

points = (w//2-w//100*20,h//2-h//100*20), (w//2+w//100*20, h//2-h//100*20), (w//2,h//2+h//100*20)

#image = Image.new('RGB', (0, 255, 255))
#draw = ImageDraw.Draw(im)
draw.polygon(points, fill=1)
print('end')
image.show()# outline='red', fill='blue'
#im.save('triangle.jpg')
image.save("/home/goto/Desktop/goto Misha 2018/SportCar(triangle).jpg")
