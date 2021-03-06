
from bs4 import BeautifulSoup
import requests
#Spiro Agnew
page = requests.get("https://en.wikipedia.org/wiki/Spiro_Agnew")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Alben W. Barkley
page = requests.get("https://en.wikipedia.org/wiki/Alben_W._Barkley")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#George H.W Bush
page = requests.get("https://en.wikipedia.org/wiki/George_H._W._Bush")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Calvin Coolidge
page = requests.get("https://en.wikipedia.org/wiki/Calvin_Coolidge")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Charles Curtis
page = requests.get("https://en.wikipedia.org/wiki/Charles_Curtis")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Charles G. Dawes
page = requests.get("https://en.wikipedia.org/wiki/Charles_G._Dawes")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Charles W. Fairbanks 
page = requests.get("https://en.wikipedia.org/wiki/Charles_W._Fairbanks")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Gerald Ford
page = requests.get("https://en.wikipedia.org/wiki/Gerald_Ford")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#John Nance Garner
page = requests.get("https://en.wikipedia.org/wiki/John_Nance_Garner")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Hubert Humphrey
page = requests.get("https://en.wikipedia.org/wiki/Hubert_Humphrey")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Lyndon B. Johnson
page = requests.get("https://en.wikipedia.org/wiki/Lyndon_B._Johnson")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Thomas Marshall
page = requests.get("https://en.wikipedia.org/wiki/Thomas_R._Marshall")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Al Gore
page = requests.get("https://en.wikipedia.org/wiki/Al_Gore")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Walter Mondale
page = requests.get("https://en.wikipedia.org/wiki/Walter_Mondale")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Richard Nixon 
page = requests.get("https://en.wikipedia.org/wiki/Richard_Nixon")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Dan Quayle
page = requests.get("https://en.wikipedia.org/wiki/Dan_Quayle")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Nelson Rockerfeller 
page = requests.get("https://en.wikipedia.org/wiki/Nelson_Rockefeller")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Teddy Roosevelt
page = requests.get("https://en.wikipedia.org/wiki/Theodore_Roosevelt")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#James S. Sherman
page = requests.get("https://en.wikipedia.org/wiki/James_S._Sherman")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Harry S. Truman 
page = requests.get("https://en.wikipedia.org/wiki/Harry_S._Truman")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#Henry A. Wallace 
page = requests.get("https://en.wikipedia.org/wiki/Henry_A._Wallace")
soup = BeautifulSoup(page.content, 'html.parser')
object = soup.find(id="content")
items = object.find_all(class_="infobox vcard")
final = items[0]
print(final.prettify())
#conversion to .csv
import pandas as pd
nme = ["Spiro Agnew", "Alben W. Barkley","George H.W Bush", "Calvin Coolidge","Charles Curtis","Charles G. Dawes","Charles W. Fairbanks","Gerald Ford", "John Nance Garner", "Hubert Humphrey", "Lyndon B. Johnson", "Thomas Marshall", "Al Gore", "Walter Mondale", "Richard Nixon", "Dan Quayle", "Nelson Rockerfeller", "Teddy Roosevelt", "James S. Sherman", "Harry S. Truman", "Henry A. Wallace"] 
prec = ["Hubert Humphrey", "Harry S. Truman","Walter Mondale","Thomas R. Marshall","Charles G. Dawes","Calvin Coolidge","Theodore Roosevelt","Spiro Agnew","Charles Curtis","Lyndon B. Johnson","Richard Nixon","James S. Sherman","Dan Quayle","Nelson Rockefeller","Alben W. Barkley","George H. W. Bush","Gerald Ford","Garret Hobart","Charles W. Fairbanks","Henry A. Wallace","John Nance Garner"]
prty = ["Republican","Democratic","Republican","Republican","Republican","Republican","Republican","Republican","Democratic","Democratic","Democratic","Democratic","Democratic","Democratic","Republican","Republican","Republican","Republican","Republican","Democratic","Democratic"]
succ = ["Gerald Ford", "Richard Nixon","Dan Quayle","	Charles G. Dawes","John Nance Garner","Charles Curtis","James S. Sherman","Nelson Rockefeller","Henry A. Wallace","Spiro Agnew","Hubert Humphrey","Calvin Coolidge","Dick Cheney","George H. W. Bush","Lyndon B. Johnson","Al Gore","	Walter Mondale","Charles W. Fairbanks","Thomas R. Marshall","Alben W. Barkley","Harry S. Truman"]
dict = {'Name of Vice President ': nme, 'Preceded By': prec, 'Succeeded By': succ, 'Political Party':prty}        
df = pd.DataFrame(dict) 
df.to_csv('20thCenturyUSVicePresidents.csv')
