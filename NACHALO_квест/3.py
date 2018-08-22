import math
bound = 600851475143
#bound = 13195
maks = 1

def is_prime(num):
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
num = math.ceil(math.sqrt(bound))
for i in range(3, num):
    if bound % i == 0:
        if is_prime(i):
            maks = i

print(maks)


    
