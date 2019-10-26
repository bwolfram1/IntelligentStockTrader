import requests
from bs4 import BeautifulSoup


technicals = {}
stock = 'msft'
def getTech(s):
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
    return technicals

