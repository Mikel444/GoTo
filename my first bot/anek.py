import telebot

import random

a1 = 'python повесился'
a2 = 'AMIGO умер'
a3 = 'ты крутой программист'

reply = 0
numder = random.randint(1, 3)

if numder == 1:
    reply = a1
    
if numder == 2:
    reply = a2
    
if numder == 3:
    reply = a3



token = "664867764:AAHHJ5J_UdYDwR5nLMGkGsxysmJOb2OO0_E"
bot = telebot.TeleBot(token=token)

telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Привет, я Анекбот, отпиши мне  /anek и я пришлю тебе шутку")
def help(message):
    user = message.chat.id
    bot.send_message(user, "Напиши мне /anek и я отправлю тебе анекдот. Всё просто")

@bot.message_handler(content_types=['text'])
def echo(message):
    user = message.chat.id
    text = message.text

    if text == '/anek':
        bot.send_message(user, reply)
    else:
        bot.send_message(user, '''Отправь мне /anek и я отправлю тебе ещё шутку''')

bot.polling(none_stop=True)
