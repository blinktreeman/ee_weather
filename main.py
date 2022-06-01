import telebot
from telebot import types
import settings
import view
import get_weather

bot = telebot.TeleBot(settings.TELE_BOT_TOKEN)


@bot.message_handler(commands=['help'])
def help(message):
    mess = 'Чтобы узнать погоду в городе\n'
    mess += 'введите /weather "название города"'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['weather'])
def weather(message):
    args = message.text.split()
    city_string = ''
    if len(args) > 1:
        city_string = ' '.join(args[1:])
    get_weather.get_meteo(city_string)
    mess = view.html_view()
    bot.send_message(message.chat.id, mess, parse_mode='html')

bot.polling(none_stop=True)
