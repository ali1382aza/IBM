import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
content =response.text

soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())
# print(content)

information = soup.find('div',class_='tab-content')

for inf in information :
    if (inf!=None):
        country = inf.find('a',class_='mt_a')
        print(country)