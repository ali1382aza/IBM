import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

information = soup.find_all('div',class_='tab-content')
numbers = information.find_all('tr')
print(numbers)

listl = []
for inf in information:
    countries = inf.find_all('a',class_='mt_a').text
    listl.append([countries])

x=0
for numb in numbers :
    num = numb.find('td')
    for nu in num :
        x+=1
        if x==3 or x==5 or x==7 or x==13:
            listl.append([nu])
            
    x=0

complete = pd.DataFrame(listl)
complete.to_csv('D:\project_corona.csv' , index=False)
