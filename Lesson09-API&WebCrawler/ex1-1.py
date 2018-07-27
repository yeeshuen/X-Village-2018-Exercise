import json
import requests

url = 'https://www.metaweather.com/api/location/2306179/2018/07/18'
r = requests.get(url)
r.encoding = 'utf-8'

weather= json.loads(r.text)
print(r.text)

print('='*40)

print(weather['weather_state_name'])