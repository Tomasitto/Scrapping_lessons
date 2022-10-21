
from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

sp = []
#ad = {'1': ['name', 'brand', 'model', 'type', 'material', 'screen', 'description', 'count',  'price'],
#      '2': ['name', 'brand', 'dig', 'material', 'screen', 'price'],
#      '3': ['name', 'brand', 'type', 'input', 'game', 'price'],
#      '4': ['name', 'brand', 'factor', 'capacity', 'volume', 'price'],
#      '5': ['name', 'brand', 'type', 'color', 'type_head_set', 'price']
#}
for i in range(1, 100):
    
    link = f'https://parsinger.ru/html/mouse/3/3_{i}.html'
    boot = requests.get(url=link)
    boot.encoding = 'utf-8'
    if str(boot.status_code) != '200':
        break
    soup = BeautifulSoup(boot.text, 'lxml')
    name = soup.find_all('p', id='p_header')
    article = soup.find_all('p', class_='article')
    desc = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')]
    stock = soup.find_all('span', id='in_stock')
    price = soup.find_all('span', id='price')
    
    for name, article, desc, stock, price in zip(name, article, desc, stock, price):
        print(i)
        dc = {}
        input_desc = {}
        dc['categories'] = 'game_mouse'
        dc['name'] = name.text
        dc['article'] = article.text.split(':')[1]
        input_desc['brand'] = desc[0].split(':')[1]
        input_desc['model'] = desc[1].split(':')[1]
        input_desc['type']= desc[2].split(':')[1]
        input_desc['game']  = desc[3].split(':')[1]
        input_desc['light']  = desc[4].split(':')[1]
        input_desc['size']  = desc[5].split(':')[1]
        input_desc['sensetive']  = desc[6].split(':')[1]
        input_desc['link']  = desc[7].split(':')[1]
        dc['description'] = input_desc
        dc['stock'] = stock.text.split(':')[1]
        dc['price'] = price.text
        sp.append(dc)
        
    
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(sp, file, indent = 4, ensure_ascii=False)



        