from bs4 import BeautifulSoup
import requests
import json
import csv


#url ='https://health-diet.ru/table_calorie'

headers = {
           'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'


}
#req = requests.get(url, headers=headers)
#src = req.text
##print(src)
#with open('index.html', 'w', encoding='utf-8') as file:
#    file.write(src) 
#
#
#
#with open('index.html', encoding='utf-8') as file:
#    src = file.read()
#
#soup = BeautifulSoup(src, 'lxml')
#
#
#all_categories_dict = {}
#links = soup.find_all(class_='mzr-tc-group-item-href')
#for i in links:
#    link_text = i.text
#    link_href= 'https://health-diet.ru' + i.get('href')
#
#    all_categories_dict[link_text] = link_href
#
#
#with open('all_categories_dict', 'w', encoding='utf-8') as file:
#    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
#
#
with open('C:\\Dev\\parcing\\all_categories_dict', encoding='utf-8') as file:
    all_categories = json.load(file)

count = 0
length = len(all_categories)
product_info = []
for name, href in all_categories.items():
    if count <= length:
        rep = [',', ' ', '-', '\'']
        for i in rep:
            for j in name:
                name = name.replace(i, '_')
        req = requests.get(href, headers=headers)
        src = req.text

    
        with open(f'C:\\Dev\\parcing\\lesson2\\data\\{count}_{name}.html', 'w', encoding='utf-8') as file1:
            file1.write(src) 

        with open(f'C:\\Dev\\parcing\\lesson2\\data\\{count}_{name}.html', encoding='utf-8') as file1:
            data = file1.read()

        soup = BeautifulSoup(data, 'lxml')
        
        #првоерка на наличие категорий
        alert = soup.find(class_='uk-alert-danger')
        if alert is not None:
            continue


        table_header = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
        
        product = table_header[0].text
        calories = table_header[1].text
        protein = table_header[2].text
        fats = table_header[3].text
        carbon = table_header[4].text

        with open(f'C:\\Dev\parcing\\lesson2\\csv_files\\{count}_{name}.csv', 'w', encoding='utf-8') as file2:
            writer = csv.writer(file2)
            writer.writerow(
                (product,
                calories,
                protein,
                fats,
                carbon

                )
            )

        product_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
        for i in product_data:
            c = i.find_all('td')
            title = c[0].find('a').text
            calories = c[1].text
            protein = c[2].text
            fats = c[3].text
            carbon = c[4].text

            with open(f'C:\\Dev\parcing\\lesson2\\csv_files\\{count}_{name}.csv', 'a', encoding='utf-8') as file2:
                writer = csv.writer(file2)
                writer.writerow(
                    (title,
                    calories,
                    protein,
                    fats,
                    carbon

                    )
                )

            info_dict = {'title': title,
                         'calories': calories,
                         'protein': protein,
                         'fats': fats,
                         'carbon': carbon}


            product_info.append(info_dict)

        with open(f'C:\\Dev\\parcing\\lesson2\\json_files\\{count}_{name}.json', 'w', encoding='utf-8') as file3:
            json.dump(product_info, file3, indent=4, ensure_ascii=False)
            
        product_info = []
        count+=1
        print(f'Идет парсинг инфы, сделано {count} из {length}')

