#請去資料來源下載 aqi 的 csv 格式
#aqi.csv 是 7/5 全台灣空氣指數的資料，讀取這個檔案
#找出 aqi 最低的數值出現的地區，並且數值是多少
#印出答案： XX 空氣最好，AQI 是 XX
import csv


AQI_INDEX = 2
SITE_INDEX = 0


with open('aqi.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)

    sitename = []
    aqix = []
    is_first_line = []
    is_first_line = True
    
    for row in reader:
        if is_first_line or not row[AQI_INDEX]:
            is_first_line = False
            continue
        sitename.append(row[SITE_INDEX])
        aqix.append(int(row[AQI_INDEX]))
    
    min_aqi = min(aqix)
    min_aqi_site = sitename[aqix.index(min_aqi)]

print('{}空氣最好， AQI是{}'.format(min_aqi_site, min_aqi))
