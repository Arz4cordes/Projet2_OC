"""import urllib.request
with urllib.request.urlopen('http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html') as f:
    print(f.read(5000))
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])"""


### requests pour récupérer le contenu de la page,
### bs4 pour récupérer une partie des données à partir de tags par exemple
### scrapy fait à la fois la fonction de requests et de récupration, et permet de traiter des gros volumes

import requests
from bs4 import BeautifulSoup
bookInformations = []
url = 'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html'
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text,'lxml')
    table = soup.findAll('table')
    for tr in table:
        information = tr.txt
        bookInformations.append(information)
    print(bookInformations)
