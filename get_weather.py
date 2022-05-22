import requests
import json
import dadata
import settings


dadata = dadata.Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET)
result = dadata.clean("address", "новый порт")
print(result['geo_lat'])
print(result['geo_lon'])
print(result['result'])

lat = result['geo_lat']
lon = result['geo_lon']
url = 'https://api.openweathermap.org/data/2.5/forecast'
response = requests.get(url, params={'lat': lat, 'lon': lon,
                                     'exclude': 'current', 'units': 'metric',
                                     'lang': 'ru', 'appid': settings.OWM_API_KEY})
data = json.loads(response.text)

print(data)
