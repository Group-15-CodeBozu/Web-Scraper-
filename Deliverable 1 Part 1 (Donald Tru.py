
#****First part of deliverable 1*****

#=================getting the response code=================

import requests

response = requests.get(
	url="https://en.wikipedia.org/wiki/Donald_Trump",
)
print(response.status_code)

#=================printing the page title=================

import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Donald_Trump",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)

#=================extracting data from card=================

from bs4 import BeautifulSoup
import requests
page = requests.get("https://en.wikipedia.org/wiki/Donald_Trump")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#conversion to .csv
import pandas as pd
nme = ["Donald Trump"] 
bday = ["June 14, 1946 (age 75)"]
bplace = ["Queens, New York City, U.S."]
prty = ["Republican Party"]
dict = {'Name': nme, 'Date of Birth and Age': bday, 'Born In': bplace, 'Political Affiliation':prty}        
df = pd.DataFrame(dict) 
df.to_csv('DonaldTrumpBio.csv') 
 
