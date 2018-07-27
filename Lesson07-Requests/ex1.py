import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

with open('music_show.json','w',encoding='utf-8') as f:
    f.write(response.text)

with open('music_show.json','r',encoding='utf-8') as f:
    reader = json.load(f)
    print(reader)
    title=[i['title'] for i in reader]
    startDate=[j['startDate'] for j in reader]
    endDate=[k['endDate'] for k in reader]

with open('music_show.txt','w',encoding='utf8') as f:
    for x,y,z in zip(title,startDate,endDate):
        text="{}:{}~{}".format(x,y,z)
        f.write(text+'\n')
        print(text)
