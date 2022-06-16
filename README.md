# ee_weather
## Telegram bot сообщает текущую погоду по городам.
Команды бота: 
- /help
- /weather 'город'
Для работы используется API:
- DaData для геокодирования (определения координат по адресу).
- OpenWeatherMap для получения данных о погоде.
## Для работы необходимо добавить файл 'settings.py'
Содержимое файла:
```
# Telegram bot token
TELE_BOT_TOKEN = 'your_token'

# DaData token, secret
DADATA_TOKEN = 'your_token'
DADATA_SECRET = 'your_secret'

# OpenWeatherMap API key
OWM_API_KEY = 'your_key'
```
