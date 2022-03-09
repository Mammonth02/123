import requests
from bs4 import BeautifulSoup
import json

sss = []
for i in range(1, 10):
    url = f'https://shop.casio.ru/catalog/?PAGEN_1={i}'
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')

    ccc = soup.find_all(class_='product-item__link')
    sss.extend(ccc)

chasy = []

for i in sss:
    soup = BeautifulSoup(i.text, 'lxml')
    name = soup.find('p').text.split()[1]
    cena = soup.find('p').text.split()[-2] + ' ' + soup.find('p').text.split()[-1] + soup.find('p').text.split()[-3]
    url = 'https://shop.casio.ru'+i.get('href')
    dd = [name, cena, url]
    chasy.append(dd)
    print(type(chasy))


with open('chasy/ss.json', 'w', encoding='utf-8') as f:
    json.dump(chasy, f, indent=4, ensure_ascii=False)
