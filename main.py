import turtle

#import des fichiers
from lireLaby import *
from affichage import *
from position import *
from navigation import *
from interface import *
from random_laby import *

choix = input("fichier/aléatoire: ")
while choix not in ["fichier","aléatoire"]:
    print("Erreur, choix incorrect")
    choix = input("fichier/aléatoire: ")

if choix == "fichier":
    fn = input("Nom d'un fichier: ")
    while not fichier_existe(fn):
        print("Erreur, fichier inexistant")
        fn = input("Nom d'un fichier: ")
    laby, entree, sortie = labyFromFile(fn) #Chargement du fichier labyrinthe
elif choix == "aléatoire":
    print("rand")
    entree = (0,0)
    sortie = (19,14)
    laby = random_generate(20,15,entree,sortie)

print()

#Affichage sous forme de matrice du labyrinthe
for ligne in laby:
    for nbr in ligne:
        print(nbr, end="")
    print()#Saut de ligne
print("Entrée:",entree)
print("Sortie:",sortie)

#Stockage de toutes les informations du fichier dans un dictionnaire
dicoJeu = {"laby":laby,"entrée":entree,"sortie":sortie, "turtle":turtle, "chemin":[]}

afficheTextuel(dicoJeu)

turtle.Screen().setup(1000,800)#Taille de la fenêtre

#Paramètres turtle rapide
turtle.delay(0)
turtle.speed(0)
afficheGraphique(dicoJeu)

#Positionnement de la turtle sur l'entrée
position_depart(dicoJeu)

turtle.onscreenclick(lambda x,y: testClic(x,y,dicoJeu)) #Quand on clique sur une cellule on print son type et sa position
map_keys(dicoJeu)#On donne le contrôle manuel à l'utilisateur
create_inter(dicoJeu)

turtle.mainloop()