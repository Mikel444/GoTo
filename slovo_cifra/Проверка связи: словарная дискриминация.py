words = []

text = input('напишите текст:')
words = text.split()
print(words)

for word in words:
    if word[0].lower() == 'а':
        print(word+';')
