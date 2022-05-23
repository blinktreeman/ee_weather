# Models

weather_model = {'city': 'Новый порт',
                 'weather_description': 'солнечно',
                 'temperature': '0',
                 'pressure': '750',
                 'humidity': '100',
                 'wind_speed': '0',
                 'wind_direction': 'северный'
                 }


def init(current, city):
    weather_model['city'] = city
    weather_model['weather_description'] = current['weather'][0]['description']
    weather_model['temperature'] = current['main']['temp']
    weather_model['pressure'] = current['main']['pressure']
    weather_model['humidity'] = current['main']['humidity']
    weather_model['wind_speed'] = current['wind']['speed']
    if 33.75 > current['wind']['deg'] > 0 and 360 > current['wind']['deg'] > 326.25:
        weather_model['wind_direction'] = 'северный'
    elif 123.75 > current['wind']['deg'] > 56.25:
        weather_model['wind_direction'] = 'восточный'
    elif 236.25 > current['wind']['deg'] > 146.25:
        weather_model['wind_direction'] = 'южный'
    elif 303.75 > current['wind']['deg'] > 236.25:
        weather_model['wind_direction'] = 'западный'

    return weather_model
