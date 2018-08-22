import telebot
import random

words =[]

chislo = random.randint(1, 1000)

token = "664867764:AAHHJ5J_UdYDwR5nLMGkGsxysmJOb2OO0_E"

telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:TyhoRuiGhj1874@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user,"Я загадал число от 1 до 1000. Попробуй отгадать его, а я буду направлять тебя словами БОЛЬШЕ или МЕНЬШЕ")

@bot.message_handler(commands=['help'])
def help(message):
    user = message.chat.id
    bot.send_message(user,"РЕКЛАМА...")

@bot.message_handler(content_types=['text'])  
def echo(message):
    text = message.text
    user = message.chat.id
    try:
        text = int(text)
    except:
        bot.send_message(user, "напиши число от  1 до 1000")
        return
    if text > chislo:
        bot.send_message(user, "МЕНЬШЕ")
    if text < chislo:
        bot.send_message(user, "БОЛЬШЕ")
    if text == chislo:
        bot.send_message(user, "УГАДАЛ, введите /start чтобы начать заново.")
    if text < 0 or text >1000:
        bot.send_message(user, "напиши число от  1 до 1000")
        
bot.polling(none_stop=True)
