import json
import requests

url = 'https://www.metaweather.com/api/location/2306179/2018/07/18'
r = requests.get(url)
r.encoding = 'utf-8'

json_dict = json.loads(r.text)
print(json_dict[0])s