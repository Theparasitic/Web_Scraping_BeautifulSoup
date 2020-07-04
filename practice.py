#https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

import requests
from bs4 import BeautifulSoup
import csv
# Collect and parse first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')
#remove last links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

#create a file
f=csv.writer(open('names.csv','w'))
f.writerow(['Name','Link'])


# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')


# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')
##for i in artist_name_list_items:
##    print(i.prettify())

##for artist_name in artist_name_list_items:
##    names = artist_name.contents[0]
##    print(names)

##
##for artist_name in artist_name_list_items:
##    names=artist_name.contents[0]
##    links='https://web.archive.org' + artist_name.get('href')
##    print(names)
##    print(links)
##f = csv.writer(open('z-artist-names.csv', 'w'))
##f.writerow(['Name', 'Link'])

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')

    # Add each artist’s name and associated link to a row
    f.writerow([names, links])
