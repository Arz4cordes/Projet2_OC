
import requests
from bs4 import BeautifulSoup


 # la fonction product_detail va sur la page d'un produit et récupère les informations demandées,
 # puis écrit ces informations dans une liste books             
def product_detail(directory_name,link,book):
    book_informations = ['info1','info2','info3','info4','info5','info6','info7','info8','info9','info10']
    try:
        url = 'http://books.toscrape.com/catalogue/{titre}/index.html'.format(titre=book)
        response = requests.get(url)
        #recupere l'url de la page produit

        if response.ok:
            response.encoding='utf-8'
            soup = BeautifulSoup(response.text,'html.parser')
            #print(book)
            #recupere le code source html de la page
    
            book_informations[0]=url
            # ajoute l'URL de la page produit

            titre=soup.find('h1')
            book_informations[2]=titre.string
            #recupere et ajoute le titre
    
            detail_produit = soup.find_all('td')
            book_informations[1] = detail_produit[0].string
            book_informations[3] = detail_produit[2].string
            book_informations[4] = detail_produit[3].string
            book_informations[5] = detail_produit[5].string
            # recupere et ajoute le code produit,
            # le prix HT,
            # le prix TTC,
            # et l'état du stock
            
  
            paragraphe = soup.find_all('p')
            p = paragraphe[2]
            note = p['class']
            book_informations[8] = note[1]
            #recupere et ajoute la note
            p = paragraphe[3]
            describe = p.string
            if describe != None:
                describe = describe.replace(";",",")
                book_informations[6] = describe 
            #recupere et ajoute la decription du livre

            listes = soup.find_all('li')
            l = listes[2]
            category = l.text
            category = category.replace('\n','')
            book_informations[7] = category                    
            #récupère et ajoute la catégorie
    
            image_produit = soup.find('img')
            path_image = image_produit.get('src')
            url_image = path_image.replace("../../","http://books.toscrape.com/")
            book_informations[9] = url_image
            #recupere et ajoute le lien de l'image du produit

            image_response=requests.get(url_image)
            if image_response.ok:
                image_link = directory_name + '/' + link + '/' + book + ".jpg"
                with open(image_link,'wb') as f:
                    f.write(image_response.content)
            #extrait l'image et l'enregistre dans un dossier local        
            
            return book_informations
    except:
        print("L'accès au produit ",book,"ne s'est pas parfaitement déroulé")
        return book_informations

# Test du module books_information sans passer par les autres programmes        
if __name__ == "__main__":
    result = product_detail("datas_retrieval","classics_6","alice-in-wonderland-alices-adventures-in-wonderland-1_5")
    print(result)





    

