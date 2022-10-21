
import requests
from bs4 import BeautifulSoup
import csv

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:

    writer = csv.writer(file, delimiter=';')


for i in range(1, 5):
    for j in range(1, 6):
        url = f'https://parsinger.ru/html/index{j}_page_{i}.html'
        link = requests.get(url=url)
        link.encoding='utf-8'
        soup = BeautifulSoup(link.text, 'lxml')

        name= soup.find_all('a', class_='name_item')
        brand = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        factor = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        capacity = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        volume = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = soup.find_all('p', class_='price')

        for name, brand, factor, capacity, volume, price in zip(name, brand, factor, capacity, volume, price):
            print(brand)
            flatten = name.text, *[x.split(':')[1].strip() for x in brand if x],price.text

            file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)

        print(f'страница {i} добавлена')