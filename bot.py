import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import token
from logic import *

bot = telebot.TeleBot(token)

def gen_markup_for_text():
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton('Получить ответ', callback_data='text_ans'),
                   InlineKeyboardButton('Перевести на en', callback_data='to_en'),
                   InlineKeyboardButton('Перевести на ru', callback_data='to_ru'),
                   InlineKeyboardButton('Перевести на de', callback_data='to_de'),
                   InlineKeyboardButton('Перевести на zh', callback_data='to_zh'))
        
        return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    obj = TextAnalysis.memory[call.from_user.id][-1]
    if call.data == "text_ans":
        bot.send_message(call.message.chat.id, obj.response)
    elif call.data == "to_en":
        bot.send_message(call.message.chat.id,  obj.translation)
    elif call.data == "to_ru":
        bot.send_message(call.message.chat.id,  obj.translation_ru)
    elif call.data == "to_de":
        bot.send_message(call.message.chat.id,  obj.translation_de)
    elif call.data == "to_zh":
        bot.send_message(call.message.chat.id,  obj.translation_zh)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Дополнительное задание
    TextAnalysis(message.text, message.from_user.id)
    bot.send_message(message.chat.id, "Я получил твое сообщение! Что ты хочешь с ним сделать?", reply_markup=gen_markup_for_text())

bot.infinity_polling(none_stop=True)