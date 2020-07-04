import requests
from bs4 import BeautifulSoup
import csv
url='https://www.investindia.gov.in/bip/resources/list-ngos-providing-relief-during-covid-19'
req=requests.get(url)#reuqest's object
soup=BeautifulSoup(req.text, "html.parser")#BeautifulSoup's object
#print(soup)
ngo=soup.find('div',{'class':'field field--name-body field--type-text-with-summary field--label-hidden field__item'})
table = ngo.find_all('table')[0]
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

