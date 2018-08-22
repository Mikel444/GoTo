s = str(input('введите фразу:'))
length = len(s)
print('')
while length >= 0:
    print(s[0:length])
    length = length - 1

