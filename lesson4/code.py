from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
url = 'https://tury.ru/hotel/?cn=0&ct=0&cat=0&txt_geo=&srch=&s='

sp = []
def get_data(url):
    headers = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '45',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    for i in range(0, 100, 20):
        r = requests.get(url=url+str(i))

        soup = BeautifulSoup(r.text, 'lxml')
        hotel_cards = soup.find_all('div', class_='reviews-travel__item')

        for hotel_href in hotel_cards:
            sp.append(hotel_href.find('a').get('href'))

        with open('C:\\Dev\\parcing\\lesson4\\links.txt', 'w', encoding='utf-8') as file:
            for i in sp:
                file.write(i+'\n')
        print(1)

def get_data_from_page():

    with open('C:\\Dev\\parcing\\lesson4\\links.txt', 'r', encoding='utf-8') as file:
        big_data = []
        for url in file:
            data = {}
            url = url.rstrip()
            r = requests.get(url=url)
            soup = BeautifulSoup(r.text, 'lxml')
            name = soup.find('li', class_='hotel_info_block').find('h3').text
            rating = soup.find('td', class_='rating_val_big').text.split()[0]
            data['name'] = name
            data['rating'] = rating
            big_data.append(data)
            print('dumping data..')
    with open('C:\\Dev\\parcing\\lesson4\\data_hotels.json', 'w', encoding='utf-8') as file1:
        json.dump(big_data, file1, indent=3)




    


    

def main():
    get_data(url)
    get_data_from_page()

if __name__ == '__main__':
    main() 