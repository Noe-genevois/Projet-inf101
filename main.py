import lireLaby
import turtle

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

#--------------------- Affichage du labyrinthe ---------------------
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


def carre(t:turtle,cote:int,couleur:str="black"):
    """Dessine un carré plein"""
    #Paramètres pour la couleur
    t.fillcolor(couleur)
    t.color(couleur)
    #On commence à dessiner
    t.pendown()
    t.begin_fill()
    #Dessin de chaque côté du carré
    for i in range(4):
        t.forward(cote)
        t.right(90)
    #Fin du dessin
    t.penup()
    t.end_fill()

def turtle_flash(t:turtle):
    """Paramètre la turtle pour qu'elle dessine rapidement"""
    #I am speed
    turtle.delay(0)
    t.speed(0)

def afficheGraphique(dicoJeu:dict,t:turtle,origine:tuple[float,float]=(-400,400),epaisseur_cellule:int=40):
    """Affichage graphique avec turtle du labyrinthe, case blanche=passage, noire=mur, verte=entrée, rouge=sortie
    l'origine correspond au coin supérieur gauche"""
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])
    #Paramètres de départ pour la turtle
    t.penup()
    t.goto(origine)
    t.setheading(0)#dirigé vers la droite
    #itération de chaque cellule du labyrinthe
    for y in range(hauteur):
        for x in range(largeur):
            if laby_liste[y][x] == 1:#si la cellule est un mur
                carre(t,epaisseur_cellule)
            elif [y,x] == dicoJeu["entrée"]:#entrée
                carre(t,epaisseur_cellule,"green")
            elif [y,x] == dicoJeu["sortie"]:#sortie
                carre(t,epaisseur_cellule,"red")
            #si on a juste un passage on effectue seulement le décalage
            t.forward(epaisseur_cellule)#Décalage pour passer à la cellule suivante de la ligne
        #Passage à la ligne du dessous
        origine = (origine[0],origine[1]-epaisseur_cellule)
        t.goto(origine)

#--------------------- Positionnement de la tortue ---------------------
def pixel2cell(position:tuple[float,float], origine:tuple[float,float]=(-400,400),epaisseur_cellule:int=40):
    x,y = position
    x-origine[0]


t = turtle.Turtle()
turtle_flash(t)
afficheGraphique(dicoJeu,t)
turtle.done()#garde la fenêtre ouverte