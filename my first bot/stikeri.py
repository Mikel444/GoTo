import telebot
import random

# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

token = "664867764:AAHHJ5J_UdYDwR5nLMGkGsxysmJOb2OO0_E"
bot = telebot.TeleBot(token=token)
stickers = []

@bot.message_handler(content_types=['sticker'])
def echo(message):
    user = message.chat.id
    sticker = message.sticker.file_id

    stickers.append(sticker)

    bot.send_sticker(user,random.choice(stickers))

bot.polling(none_stop=True)
