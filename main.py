# -*- coding: utf-8 -*-
import telebot
from telebot import types
import os

yarr = os.environ.get('YARR', None)

bot = telebot.TeleBot(yarr)

@bot.message_handler(commands=['fuck'])
def fuck(message):
    sent = bot.send_message(message.chat.id, "you've pressed 'fuck'")
    bot.register_next_step_handler(sent, next_step)

@bot.message_handler(commands=['test'])
def test(message):
    sent = bot.send_message(message.chat.id, "you've pressed 'test'")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

    keyboard.add(*[types.KeyboardButton(str(n+1)) for n in range(10)])

    #keyboard.add(types.KeyboardButton('me'),types.KeyboardButton('so'),types.KeyboardButton('horny'))

    sent_method = bot.send_message(message.chat.id, 'rate this shit', reply_markup=keyboard)

    bot.register_next_step_handler(sent_method, choosen)

def choosen(message):
    sent_method = bot.send_message(message.chat.id, "thanks for rate (%r)"%("*"*int(message.text)), reply_markup=types.ReplyKeyboardRemove())
   # bot.register_next_step_handler(sent_method, choosen)
    
def next_step(message):
    bot.send_message(message.chat.id, "message sent from 'next_step' callback")

def new_game():
    # bot.add_message_handler({'fooock' : 'yoooou'})
    bot.polling()

