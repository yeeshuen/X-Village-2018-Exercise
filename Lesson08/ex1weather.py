import json
import requests

url = 'https://www.metaweather.com/api/location/2306179/2018/07/18'
r = requests.get(url)
r.encoding = 'utf-8'

json_dict = json.loads(r.text)
print(json_dict[0])

print("="*40)
print("weather_state:",json_dict[0]['weather_state_name'])