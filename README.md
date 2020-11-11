Projet2_OC
Pour lancer le scrapping du site Books to Scrape:

1. Créer un environnement virtuel avec la commande suivante en ligne de commande:  
python -m venv env

2. Activer cet environnement virtuel avec la commande suivante sous windows:  
env/scripts/activate
(si vous êtes avec un autre système d'exploitation, écrire par exemple source env/bin/activate)

3. Installer les paquets nécessaires pour que le programme fonctionne, avec la commande:  
pip install -r requirements.txt
(cela va importer les paquets BeautifulSoup et Requests)

4. Lancer l'éxécution du programme à l'aide de la commande suivante:  
python books_scraping.py

5. Il vous sera demandé de nommer un repertoire dans lequel les données récupérées seront chargées 
(le nom ne doit contenir que des lettres minuscules, des espaces, ou des underscore _ )

Note: le programme books_scraping.py va utiliser le module books_list, qui va utiliser lui même le module book_detail

