import telebot
from telebot import types
import settings

bot = telebot.TeleBot(settings.TELE_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton()

    markup.add(types.InlineKeyboardButton('Пумц на Яндекс', url='http://www.yandex.ru'))
    bot.send_message(message.chat.id, '<u>Идите на яндекс</u>', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Пумц на Яндекс', url = 'http://www.yandex.ru'))
    bot.send_message(message.chat.id, '<u>Идите на яндекс</u>', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'И тебе хеллоу', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('its_worked.gif', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Моя твоя непонимайт', parse_mode='html')
        #bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, '<u>Гуд sticker я я</u>', parse_mode='html')


bot.polling(none_stop=True)
