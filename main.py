import turtle

#import des fichiers
from lireLaby import *
from affichage import *
from position import *
from navigation import *


fn = input("Nom d'un fichier: ")
laby, entree, sortie = labyFromFile(fn) #Chargement du fichier labyrinthe
print()

#Affichage sous forme de matrice du labyrinthe(liste à 2 dimensions)
for ligne in laby:
    for nbr in ligne:
        print(nbr, end="")
    print()
print("Entrée:",entree)
print("Sortie:",sortie)

#Stockage de toutes les informations du fichier dans un dictionnaire
dicoJeu = {"laby":laby,"entrée":entree,"sortie":sortie, "turtle":turtle, "commandes":[]}

afficheTextuel(dicoJeu)

#Paramètres pour accélérer la turtle
turtle.delay(0)
turtle.speed(0)
afficheGraphique(dicoJeu)

turtle.onscreenclick(lambda x,y: testClic(x,y,dicoJeu)) #Quand on clique sur une cellule on print son type et sa position

#Positionnement de la turtle sur l'entrée
j_entree,i_entree = dicoJeu["entrée"]
turtle.goto(cell2pixel(i_entree,j_entree,dicoJeu))


#Correspondance des touches de clavier
turtle.onkeypress(lambda : gauche(dicoJeu), "Left")
turtle.onkeypress(lambda : droite(dicoJeu), "Right")
turtle.onkeypress(lambda : haut(dicoJeu), "Up")
turtle.onkeypress(lambda : bas(dicoJeu), "Down")
turtle.listen()


turtle.mainloop()