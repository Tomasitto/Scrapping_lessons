
from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

sp = []
for i in range(1, 100):
    
    link = f'https://parsinger.ru/html/index1_page_{i}.html'
    boot = requests.get(url=link)
    boot.encoding = 'utf-8'

    if str(boot.status_code) != '200':
        break
    soup = BeautifulSoup(boot.text, 'lxml')
    name = soup.find_all('a', class_='name_item')
    desc = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = soup.find_all('p', class_='price')
    print(i)

    for name, desc, price in zip(name, desc, price):
        
        dc = {}
        dc['name'] = name.text
        dc['brand'] = desc[0].split(': ')[1]
        dc['type'] = desc[1].split(': ')[1]
        dc['material'] = desc[2].split(': ')[1]
        dc['screen']  = desc[3].split(': ')[1]
        dc['price'] = price.text
        sp.append(dc)
    print(sp)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(sp, file, indent = 4, ensure_ascii=False)


    
        