import matplotlib.pyplot as plt
import pandas as pd
url = 'http://markets.financialcontent.com/stocks/action/gethistoricaldata?Month=12&Symbol=GOOG&Range=300&Year=2017'
google_stock = pd.read_csv(url)
google_stock.head()
new_google_stock = google_stock.iloc[::-1]
new_google_stock = new_google_stock[:30]
#print(new_google_stock)
plt.figure(figsize=(10, 5))
print(new_google_stock.shape)
x = range(0,new_google_stock.shape[0])
y = new_google_stock['Open']
y1 = new_google_stock['High']
y2 = new_google_stock['Low']
print(x) 
plt.plot(x, y, color='blue', linewidth=2.0, linestyle=':') 
plt.fill_between(x, y1, y2, where=y2 >= y1, facecolor='yellow', interpolate=True)
plt.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
plt.title('google hi 03/1996');
plt.show()