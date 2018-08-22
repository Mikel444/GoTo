a = 1
b = 2
summ = 0
while a <= 4000000:
    if a % 2 == 0:
        summ += a
    c = a + b
    a = b
    b = c
print(summ)
