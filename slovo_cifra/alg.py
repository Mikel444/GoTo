import random

key = 40 #int(input('input: '))
a = [1,1,2,2,3,40,32,3232,321,2324,1,2]
a.sort()
n = len(a)

l = 0
r = n
while l < r - 1:
    m = (l + r) // 2
    if key < a[m]:
        r = m
        #print(r)
    else:
        l = m
        #print(l)
print(m)
