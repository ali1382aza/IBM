import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

for ing in soup:
    countries = soup.find() 
# information =soup.find_all('div',class_='tab-content')
# print(information)



time.sleep(1)