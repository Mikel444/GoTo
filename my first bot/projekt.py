import telebot

words = []

token = "664867764:AAHHJ5J_UdYDwR5nLMGkGsxysmJOb2OO0_E"

telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:TyhoRuiGhj1874@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user,"")

@bot.message_handler(commands=['help'])    
def help(message):
    user = message.chat.id
    bot.send_message(user,"")

@bot.message_handler(content_types=['text'])
def echo(message):

    text = message.text
    user = message.chat.id

    while True:
        if len(words) == 0:
            words.append(text)
            print(words)
            continue
        if text in words:
            bot.send_message(user, 'это слово уже есть')
            continue
        lastWord = words[-1]
        lastLet = lastWord[-1]
        firstLet = text[0]
        if lastLet.lower() != firstLet.lower():
            bot.send_message(user, 'Последняя буква предыдущего слова не совпадает с первой этого')
            continue
        words.append(text)

    #bot.send_message(user, '')

bot.polling(none_stop=True)

############################################
