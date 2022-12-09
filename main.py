import turtle

#import des fichiers
from lireLaby import *
from affichage import afficheGraphique,afficheTextuel
from position import testClic
from navigation import position_depart
from interface import map_keys,create_inter
from random_laby import random_generate

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

screen = turtle.Screen()
screen.setup(1000,800)#Taille de la fenêtre

screen.tracer(0)#On enlève les animations Turtle pour tracer le labyrinthe quasi instantanément
afficheGraphique(dicoJeu)
position_depart(dicoJeu)
screen.tracer(1)#On remet les animations Turtle pour pouvoir voir ce qu'il se passe

turtle.onscreenclick(lambda x,y: testClic(x,y,dicoJeu)) #Quand on clique sur une cellule on print son type et sa position
map_keys(dicoJeu)#On donne le contrôle manuel à l'utilisateur
create_inter(dicoJeu)

turtle.mainloop()