# -*- coding: utf-8 -*-
import telebot
from telebot import types
import os
yarr = os.environ.get('YARR', None)
bot = telebot.TeleBot(yarr)
icon_url = "https://avatars3.githubusercontent.com/u/577316"


@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="->", callback_data="right"))
    keyboard.add(types.InlineKeyboardButton(text="<-", callback_data="left"))
    msg = bot.send_message(m.chat.id, "you must choose one of two ways", reply_markup=keyboard)

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    result = types.InlineQueryResultArticle(
             id=1, 
             title="option 1", 
             description="*you wrote* :"+query.query, 
             input_message_content= types.InputTextMessageContent("result"),
             thumb_url=icon_url, thumb_width=48, thumb_height=48)
    print(query.query)
    bot.answer_inline_query(query.id, [result])

#@bot.callback_query_handler(func=lambda c:True)
#def inline(c):
#    if c.data == 'right':
#        bot.edit_message_text(
#            chat_id=c.message.chat.id,
#            message_id=c.message.message_id,
#            text = 'turned right. you *died*.',
#            parse_mode = 'Markdown')
#    if c.data == 'left':
#        bot.edit_message_text(
#            chat_id=c.message.chat.id,
#            message_id=c.message.message_id,
#            text = "turned left. you've *get fucked*.",
#            parse_mode = 'Markdown')

#@bot.message_handler(commands=['fuck'])
#def fuck(message):
#    sent = bot.send_message(message.chat.id, "you've pressed 'fuck'")
#    bot.register_next_step_handler(sent, next_step)

#@bot.message_handler(commands=['hallo'])
#def hallo(message):
#    sent = bot.send_message(message.chat.id, "you've pressed 'fuck'")
#    bot.register_next_step_handler(sent, next_step)

#@bot.message_handler(commands=['test'])
#def test(message):
#    print('tested')
#    sent = bot.send_message(message.chat.id, "you've pressed 'test'")

#    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

#    keyboard.add(*[types.KeyboardButton(str(n + 1)) for n in range(10)])

#    #keyboard.add(types.KeyboardButton('me'),types.KeyboardButton('so'),types.KeyboardButton('horny'))

#    sent_method = bot.send_message(message.chat.id, 'rate this shit', reply_markup=keyboard)

#    bot.register_next_step_handler(sent_method, choosen)

#def choosen(message):
#    sent_method = bot.send_message(message.chat.id, "thanks for rate (%r)" % ("*" * int(message.text)), reply_markup=types.ReplyKeyboardRemove())
#   # bot.register_next_step_handler(sent_method, choosen)
#def next_step(message):
#    bot.send_message(message.chat.id, "message sent from 'next_step' callback")

def new_game():
    #bot.send_message(258610595, '🗿◻◻◻◻◻◻◻◻◻◻👻◻◻◻')
    #bot.edit_message_text("-_-_-",258610595,. )
    bot.polling()
    

if __name__ == '__main__':  
    new_game()

