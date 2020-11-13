
import csv
import requests
from bs4 import BeautifulSoup
import book_detail as b_detail

# la fonction books_in_category va sur la page d'une catégorie donnée,
# puis crée une liste books qui contient les livres de la catégorie:
def books_in_category(category):
    books = []
    
    url_category = 'http://books.toscrape.com/catalogue/category/books/{lien}/index.html'.format(lien=category)
    response = requests.get(url_category)
    if response.ok:
        response.encoding='utf-8'
        soup = BeautifulSoup(response.text,'html.parser')
        articles = soup.select("h3 > a")
        for article in articles:
            book = article['href']
            book = book.replace('../../../','').replace('/index.html','')
            books.append(book)

        # observe si il y a des pages suivantes, et si oui parcourt ces pages:
        page_link = soup.find("li",class_="next")
        if page_link != None:
            page = page_link.string
            the_page = 2
            url_category_other_pages='http://books.toscrape.com/catalogue/category/books/{lien}/page-'.format(lien=category)
                      
            while page == "next":
                url_category = url_category_other_pages + str(the_page) + '.html'
                response = requests.get(url_category)
                if response.ok:
                    response.encoding='utf-8'
                    soup = BeautifulSoup(response.text,'html.parser')
                    articles = soup.select("h3 > a")
                    for article in articles:
                        book = article['href']
                        book = book.replace('../../../','').replace('/index.html','')
                        books.append(book)
                    page_link = soup.find("li",class_="next")
                    if page_link == None:
                        page = "It was the last page"
                    the_page += 1
                                 
        return books
    else:
        print('Aucun livre récupéré dans cette catégorie')
        return books


# la fonction creation_csv_category crée un fichier csv
# et enregistre dedans les informations (liste books en paramètre)
# de chaque livre de la catégorie (nommée link en paramètre):
def creation_csv_category(directory_name,link,books):
    file = str(directory_name + '/'+ link + '/' + link + '.csv')
    with open(file, 'w', newline='',encoding='utf-8') as csvfile:
        informations_writer = csv.writer(csvfile,delimiter=';',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        informations_writer.writerow(['product_page_url','universal_product_code(upc)','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url'])
        # on crée le fichier csv de la catégorie avec une en tête
        
        for book in books:
            informations_writer.writerow(b_detail.product_detail(directory_name,link,book))
            # on lance le module books_information et on exécute la fonction product_detail,
            # puis on écrit les infos du livre dans une nouvelle ligne du fichier csv


# test du module books_category sans passer par le programme principal
if __name__ == "__main__":
    import os
    directory_name = "datas_retrieval"
    #os.mkdir(directory_name)
    link = "classics_6"
    link_2 = "default_15"
    os.chdir(directory_name)
    os.mkdir(link)
    os.mkdir(link_2)
    os.chdir('../')
    bic = books_in_category(link)
    bic_2 = books_in_category(link_2)
    path_modified = link.replace('catalogue/category/books/','')
    file=path_modified.replace('/index.html','')
    creation_csv_category(directory_name,link,bic)
    path_modified = link_2.replace('catalogue/category/books/','')
    file=path_modified.replace('/index.html','')
    creation_csv_category(directory_name,link_2,bic_2)


