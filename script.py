import requests
import datetime
import bs4
from emailscript import sendemails

######		SCRAPPING		######

country = '# PASTE THE COUNTRY'
response = requests.get('https://www.worldometers.info/coronavirus/country/'+country.lower()+'/')
soup = bs4.BeautifulSoup(response.text, 'lxml')

value = []
key = []
for i in soup.select('.maincounter-number span'):
	value.append(i.text)

for i in soup.select('h1'):
	key.append(i.text[:-1])

key.pop(0)
data = dict(zip(key, value))

#####		  TIME 			######

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

#####		 EMAIL 			#####

SENDER = "# PASTE YOUR GMAIL "
GOOGLE_PASS = " # PASTE YOUR APP PASSWORD "
reciever = SENDER
subject = "Daily Covid Tracker INDIA"
body = f"Date: {date}\n\nTime: {time}\n\nTotal Cases: {data['Coronavirus Cases']}\n\nTotal Deaths: {data['Deaths']}\n\nTotal Recovered: {data['Recovered']}"

sendemails(SENDER, reciever, GOOGLE_PASS, subject, body)
