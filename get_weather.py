import requests
import json
import settings
import model


def get_meteo(city):
    import dadata
    # Определяем широту, долготу по запросу
    dadata = dadata.Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
    geo_data = dadata.clean("address", city)
    if geo_data['result']:
        lat = geo_data['geo_lat']
        lon = geo_data['geo_lon']
        # Запрос метеоданных по координатам
        url = 'https://api.openweathermap.org/data/2.5/weather'
        response = requests.get(url, params={'lat': lat, 'lon': lon,
                                            'exclude': 'current', 'units': 'metric',
                                            'lang': 'ru', 'appid': settings.OWM_API_KEY})
        meteo_data = json.loads(response.text)
        model.init(meteo_data, geo_data['result'])
    else:
        print('Место не найдено!')


#print(model.weather_model['city'])
#print(model.weather_model['temperature'])

