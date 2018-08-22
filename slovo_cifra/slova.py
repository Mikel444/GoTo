words = []

while True:
    word = input('ввeдитe слово:')
    if len(words) == 0:
        words.append(word)
        print(words)
        continue
    if word in words:
        print('это слово уже есть')
        continue
    lastWord = words[-1]
    lastLet = lastWord[-1]
    firstLet = word[0]
    if lastLet.lower() != firstLet.lower():
        print('Последняя буква не совпадает с первой')
        continue
    words.append(word)
    print(words)
