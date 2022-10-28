import lireLaby

fn = input("Nom d'un fichier: ")
laby, entree, sortie = lireLaby.labyFromFile(fn) #Chargement du fichier labyrinthe
print("\n")

#Affichage sous forme de matrice du labyrinthe(liste à 2 dimensions)
for ligne in laby:
    for nbr in ligne:
        print("%5.1d"%nbr,end="")
    print("\n")
print("Entrée:",entree)
print("Sortie:",sortie)

#Stockage de toutes les informations du fichier dans un dictionnaire
dicoJeu = {"laby":laby,"entrée":entree,"sortie":sortie}

#Fonctions pour l'affichage du labyrinthe
def afficheTextuel(dicoJeu:dict):
    """Affichage textuel du labyrinthe dans dicoJeu, '#'=mur 'x'=entrée 'o'=sortie ' '=passage"""
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])
    #on parcours chaque case du labyrinthe
    for y in range(hauteur):
        for x in range(largeur):
            case = laby_liste[y][x]
            if case == 1: #la case est un mur
                print('#', end='')
            else: #case == 0, la case est un passage
                if dicoJeu["entrée"] == [y,x]:
                    print('x', end='')
                elif dicoJeu["sortie"] == [y,x]:
                    print('o', end='')
                else: # la case est un passage quelconque
                    print(' ',end='')
        print() #On change de ligne à afficher

afficheTextuel(dicoJeu)