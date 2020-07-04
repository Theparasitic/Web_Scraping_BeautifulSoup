import requests
from bs4 import BeautifulSoup
url='https://www.python.org/events/python-events/'
req=requests.get(url)#reuqest's object
#print(req.text[:200])
soup=BeautifulSoup(req.text,'lxml')#BeautifulSoup's object
"""
Tell the beautiful soup to find the main <ul> tag for the recent events
and then get all <li> events
"""
events=soup.find('ul',{'class':'list-recent-events menu'}).findAll('li')
#print(events)
"""
Loop through each of the <li> elements and extract the event details and print
"""
event_details=dict()
for event in  events:
    event_details['name']=event.find('h3').find("a").text
    event_details['location']=event.find('span',{'class':'event-location'}).text
    event_details['time']=event.find('time').text
    print(event_details)
"""
requests is usedt to execute http requests
req obj of request hold results of requests , not only page content but many other
items too such as http status codes and headers
