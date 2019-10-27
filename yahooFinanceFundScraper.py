import requests
from bs4 import BeautifulSoup
import pandas as pd

stock = ['msft','aapl','tsla','googl']
def getTech(s):
    df = pd.DataFrame()
    technicals = {}
    for stock in s:
        url = ('http://finance.yahoo.com/q/ks?s='+stock)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        tables = soup.findAll('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                title = row.find('span').get_text()
                dt = row.find(class_='Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)').get_text()
                technicals[title] = dt
        technicals['Stock'] = stock
        df = df.append([technicals])
    df = df.reset_index(drop=True)
    return df
df1 = getTech(stock)
print(df1['Price/Book'])