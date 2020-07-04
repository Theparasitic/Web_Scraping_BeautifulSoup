import requests
import request
from htmldate import find_date
import urllib
import csv
from lxml import etree
from io import StringIO
from bs4 import BeautifulSoup
keyword = input('search here: ')

page = requests.get('https://news.google.com/search?q='+keyword+'&hl=en-IN&gl=IN&ceid=IN%3Aen')
soup = BeautifulSoup(page.content, 'html.parser')
tmp=soup.find(class_='HKt8rc CGNRMc')
links=tmp.find_all('a')

###file creation
fil=csv.writer(open('news.csv','w'))
fil.writerow(['Name','Link'])

for i in links[:20]:
        print(i.get('href'))
        #title=i.contents[0]
        url=str(i.get('href'))
        url.replace(url[0],'')
        if url=='None':
            continue
        else:
            url='https://news.google.com/'+url
            url=urllib.parse.unquote(url)
            html = urllib.request.urlopen(url).read().decode('utf8')
            html[:60]
            ss = BeautifulSoup(html, 'html.parser')
            title=ss.title.text
            fil.writerow([title,url])
            


