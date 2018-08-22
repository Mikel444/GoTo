import telebot
from random import randint
token = 'токен'

telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

user_numbers = {}

@bot.message_handler(commands=['help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Это Гадайбот. Я загадываю число от 0 до 10, а ты его должен отгадать")

@bot.message_handler(commands=['start'])
def start(message):
    number = randint(0, 10)
    bot.send_message(user, 'Я загадал. Ну, угадывай давай')
    user_numbers[user] = number
    
@bot.message_handler(content_types=['text'])
def value(message):
    user = message.chat.id
    if user not in user_numbers:
        bot.send_message(user, 'напиши /start, чтобы начать')
    try:
        count = int(message.text)
    except:
        bot.send_message(user, 'Не понимаю')
        return    
    number = user_numbers[user]
    if count < number:
        bot.send_message(user, numbers, 'Больше')
        return
    if count > number:
        bot.send_message(user, numbers,  'Меньше')
        return
    bot.send_message(user, numbers, 'Ты угадал, молодец!')
    
bot.polling(none_stop=True)
