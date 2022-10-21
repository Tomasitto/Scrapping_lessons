
import requests
from bs4 import BeautifulSoup
import csv

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:

    writer = csv.writer(file, delimiter=';')
    writer.writerow([

        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'])

dc = {'1': 'watch',
      '2': 'mobile',
      '3': 'mouse',
      '4': 'hdd',
      '5': 'headphones'}

for j in range(1, 5):

    for k in range(1, 100):
        
        
        print(k)
        page_link = f'https://parsinger.ru/html/{dc[str(j)]}/{j}/{j}_{k}.html'
        req_link = requests.get(page_link)
        if str(req_link.status_code) != '200':
            break
        req_link.encoding = 'utf-8'
        soup2 = BeautifulSoup(req_link.text, 'lxml')
        name= soup2.find_all('p', id='p_header')
        article = soup2.find_all('p', class_='article')
        brand = [x.text.split('\n') for x in soup2.find_all('ul', id='description')][0]
        a, b = [brand[1]], [brand[2]]
        col = soup2.find_all('span', id='in_stock')
        price = soup2.find_all('span', id='price')
        old_price = soup2.find_all('span', id='price')
        href = [page_link]
        for name, article, a, b , col, price, old_price, href in zip(name, article, a, b, col, price, old_price, href):
            flatten = name.text, article.text.split(':')[1], a.split(':')[1], b.split(':')[1], col.text.split(':')[1],  price.text, old_price.text, href
            file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)
    print(f'страница {j} добавлена')



        