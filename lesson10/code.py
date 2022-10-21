
from textwrap import indent
import requests
from bs4 import BeautifulSoup
import json

sp = []
crrr = {'1': 'watch',
        '2': 'mobile',
        '3': 'mouse',
        '4': 'hdd',
        '5': 'headphones'}

ad = {'1': ['brand', 'model', 'type', 'screen', 'case',  'locker', 'size', 'link'],
      '2': ['brand', 'model', 'type', 'case',   'type_screen', 'screen',  'size', 'weight', 'screen_size', 'link'],
      '3': ['brand', 'model', 'type', 'game', 'light',  'size', 'sensetive', 'link'],
      '4': ['brand', 'model', 'factor', 'capacity', 'volume',  'speed', 'power', 'interface', 'link'],
      '5': ['brand', 'model', 'type', 'zone', 'microphone',  'wire', 'input', 'spec']
}
for i in range(1, 6):
    for j in range(1, 100):

        link = f'https://parsinger.ru/html/{crrr[str(i)]}/{i}/{i}_{j}.html'
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
            dc['categories'] = crrr[str(i)]
            dc['name'] = name.text
            dc['article'] = article.text.split(':')[1]
            input_desc[ad[str(i)][0]] = desc[0].split(':')[1]
            input_desc[ad[str(i)][1]] = desc[1].split(':')[1]
            input_desc[ad[str(i)][2]]= desc[2].split(':')[1]
            input_desc[ad[str(i)][3]]  = desc[3].split(':')[1]
            input_desc[ad[str(i)][4]]  = desc[4].split(':')[1]
            input_desc[ad[str(i)][5]]  = desc[5].split(':')[1]
            input_desc[ad[str(i)][6]]  = desc[6].split(':')[1]
            input_desc[ad[str(i)][7]]  = desc[7].split(':')[1]

            if len(ad[str(i)])== 10:
                input_desc[ad[str(i)][8]]  = desc[8].split(':')[1]
                input_desc[ad[str(i)][9]]  = desc[8].split(':')[1]

            if len(ad[str(i)])== 9:
                input_desc[ad[str(i)][8]]  = desc[8].split(':')[1]

            dc['description'] = input_desc
            dc['stock'] = stock.text.split(':')[1]
            dc['price'] = price.text
            sp.append(dc)


    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(sp, file, indent = 4, ensure_ascii=False)



        