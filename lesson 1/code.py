from inspect import classify_class_attrs
from bs4 import BeautifulSoup


with open('C:\\Dev\\parcing\\lesson 1\index.html', encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')


#title = soup.title
#print(title)
#print(title.text)
#print(title.string)


#ll_spand = soup.find(class_='user__info', ).find_all('span')
#
#or i in all_spand:
#   print(i.text )


#soc_links = soup.find(class_='social__networks').find('ul').find_all('a')
#print(soc_links)

#find_al = soup.find_all('a')
#
#for i in find_al:
#    i_text = i.text
#    link = i.get('href')
#    print(link, i_text)



# find_parent() adn find_parents() methods    
#find_par = soup.find(class_='user__city').find_parents()
#
#print(find_par)


# .next_element() or .find_next() and .previous_element()
#
#nexting =  soup.find(class_='social__networks').find_next()
#print(nexting)


# .find_next_sibling() and .find_previous_sibling()
col = soup.find(class_='user__avatar').find_next_sibling()
print(col)