import requests
from bs4 import BeautifulSoup
import csv
url='https://www.indiaeinfo.com/list-of-highest-donation-for-corona-in-india/'
req=requests.get(url)#reuqest's object
soup=BeautifulSoup(req.text, "html.parser")#BeautifulSoup's object
donors=soup.find('div',{'class':'entry'}).findAll('li')
#print(donors)
res=[]
for i in donors:
    res.append(i.text)
res =res[: len(res) - 6]
fil=csv.writer(open('donors.csv','w'))
fil.writerow(['Name','Amount'])
for i in res:
    x=i
    li=x.split('–')
    fil.writerow([li[0],li[1]])

