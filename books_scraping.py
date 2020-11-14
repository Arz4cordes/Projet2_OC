import requests
from bs4 import BeautifulSoup
import books_list as b_list
import os

#Programme principal:
    # aller sur la page d'accueil du site
    # récupérer les différentes catégories dans le menu latéral du site
    # lancer le module books_category:
        # le module books_category va sur la page d'une catégorie donnée,
        # puis crée une liste books qui contient les livres de la catégorie,
        # crée le fichier csv de la catégorie,
        # et enfin lance une boucle pour parcourir ces livres:
            # pour chaque livre, le module books_informations se lance:
                # le module books_informations va sur la page d'un livre,
                # puis récupère les infos sur ce livre,
                # met les infos dans un tableau books_detail,
                # et pour finit écris les infos du livre dans une nouvelle ligne du fichier csv de la catégorie


# la fonction category_list va récupérer l'ensemble des catégories de livre dans un menu latéral
# puis écris les différentes catégories dans une liste categories
def category_list():
    categories=[]
    url='http://books.toscrape.com/'
    response = requests.get(url)
    if response.ok:
        response.encoding='utf-8'
        soup = BeautifulSoup(response.text,'html.parser')
        category_listing = soup.find_all("a",limit=53)
        counter=1
        for category in category_listing:
            if counter>3:
                counter+=1
                category_link=str(category.get('href'))
                categories.append(category_link.replace('catalogue/category/books/','').replace('/index.html',''))
            else:
                counter+=1
        return categories

    else:
        print("Désolé, un problème a été rencontré lors de l'accès à la page d'accueil du site")

# la fonction directory_creation demande à l'utilisateur de nommer le répertoire
# dans lequel les données seront extraites, vérifie que le nom de dossier respecte une convention;
# puis créer ce repertoire
def directory_creation():
    directory_test = False
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_',' ']
    directory_name = "dossier"
    while directory_test == False:
        directory_name = input('Ecrivez le nom du dossier,en minuscules, dans lequel les données seront écrites (espaces et _ autorisés):')
        directory_name = str(directory_name)
        directory_test = True
        for d in directory_name:
            if d not in caracteres:
                directory_test = False
                print("Seuls les espaces, underscore, et lettres minuscules sont acceptées")
        try:
            os.mkdir(directory_name)
        except FileExistsError:
            directory_test = False
            print('Ce nom de dossier existe déjà')
    return directory_name


def main():
    directory_name = directory_creation()
    links = category_list()
    for link in links:
        print(link.upper())
        os.chdir(directory_name)
        os.mkdir(link)
        os.chdir('../')
        books = b_list.books_in_category(link)
        b_list.creation_csv_category(directory_name,link,books)
    

if __name__ == "__main__":
    main()


