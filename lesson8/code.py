
from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

sp = []
ad = {'1': ['name', 'brand', 'type', 'material', 'screen', 'price'],
      '2': ['name', 'brand', 'dig', 'material', 'screen', 'price'],
      '3': ['name', 'brand', 'type', 'input', 'game', 'price'],
      '4': ['name', 'brand', 'factor', 'capacity', 'volume', 'price'],
      '5': ['name', 'brand', 'type', 'color', 'type_head_set', 'price']
}
for i in range(1, 6):
    for j in range(1, 5):
    
        link = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        boot = requests.get(url=link)
        boot.encoding = 'utf-8'

        if str(boot.status_code) != '200':
            break
        soup = BeautifulSoup(boot.text, 'lxml')
        name = soup.find_all('a', class_='name_item')
        desc = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        price = soup.find_all('p', class_='price')

        for name, desc, price in zip(name, desc, price):
            
            dc = {}
            dc[ad[str(i)][0]] = name.text
            dc[ad[str(i)][1]] = desc[0].split(':')[1]
            dc[ad[str(i)][2]] = desc[1].split(':')[1]
            dc[ad[str(i)][3]]= desc[2].split(':')[1]
            dc[ad[str(i)][4]]  = desc[3].split(':')[1]
            dc[ad[str(i)][5]] = price.text
            sp.append(dc)
            print(dc)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(sp, file, indent = 4, ensure_ascii=False)



        