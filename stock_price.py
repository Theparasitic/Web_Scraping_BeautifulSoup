import requests
from bs4 import BeautifulSoup

def parseprice():
    req=requests.get('https://in.finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch')
    soup=BeautifulSoup(req.text,'lxml')
    price=soup.find('div',{'class':'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text
    
while True:
    print('th current price: '+str(parseprice()))
