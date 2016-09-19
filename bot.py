# -*- coding: utf-8 -*-
import telebot
import random

bot = telebot.TeleBot(input('Please, enter token:'))

text = []
with open('text') as f:
    text = f.read().splitlines()

@bot.message_handler(func=lambda message: True, content_types=['text'])
def quote(message):
    number = random.choice(text)
    bot.send_message(message.chat.id, number)

if __name__ == '__main__':
    bot.polling(none_stop=True)
