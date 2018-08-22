import random
a = 0
chislo = random.randint(1, 50)
while a != chislo:
    a = int(input('введите число:'))
    if a < chislo:
        print('число',a,'<')
    if a > chislo:
        print('число',a,'>')
print('угадал!')
