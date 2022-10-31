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


def carre(cote:int,couleur:str="black"):
    """Dessine un carré plein"""
    global turtle
    #Paramètres pour la couleur
    turtle.fillcolor(couleur)
    turtle.color(couleur)
    #On commence à dessiner
    turtle.pendown()
    turtle.begin_fill()
    #Dessin de chaque côté du carré
    for i in range(4):
        turtle.forward(cote)
        turtle.right(90)
    #Fin du dessin
    turtle.penup()
    turtle.end_fill()

def turtle_flash():
    """Paramètre la turtle pour qu'elle dessine rapidement"""
    #I am speed*
    global turtle
    turtle.delay(0)
    turtle.speed(0)

def afficheGraphique(dicoJeu:dict,origine:tuple[float,float]=(-400,400),epaisseur_cellule:int=40):
    """Affichage graphique avec turtle du labyrinthe, case blanche=passage, noire=mur, verte=entrée, rouge=sortie
    l'origine correspond au coin supérieur gauche"""
    global turtle
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])

    #Paramètres de départ pour la turtle
    turtle.penup()
    turtle.goto(origine)
    turtle.setheading(0)#dirigé vers la droite
    
    #itération de chaque cellule du labyrinthe afin de les dessiner
    for y in range(hauteur):
        for x in range(largeur):
            if laby_liste[y][x] == 1:#si la cellule est un mur
                carre(epaisseur_cellule)
            elif [y,x] == dicoJeu["entrée"]:#entrée
                carre(epaisseur_cellule,"green")
            elif [y,x] == dicoJeu["sortie"]:#sortie
                carre(epaisseur_cellule,"red")
            #si on a juste un passage on effectue seulement le décalage
            turtle.forward(epaisseur_cellule)#Décalage pour passer à la cellule suivante de la ligne
        #Passage à la ligne du dessous
        turtle.goto((origine[0],origine[1]-y*epaisseur_cellule))
    #Fin du dessin
    #On stock des informations utiles pour d'autres fonctions dépendantes de l'affichage graphique
    dicoJeu["origine_graph"] = origine
    dicoJeu["epaisseur_cellule"] = epaisseur_cellule
    dicoJeu["hauteur_graph"] = hauteur*epaisseur_cellule
    dicoJeu["largeur_graph"] = largeur*epaisseur_cellule

#--------------------- Positionnement de la tortue ---------------------
def pixel2cell(coord:tuple[float,float], dicoJeu:dict):
    """Conversion de coordonnées turtle en coordonnées dans le labyrinthe, return None si on est en dehors du labyrinthe"""
    #Vérification que les variables nécessaires existent bien dans dicoJeu (si afficheGraphique a bien été exécuté en amont)
    x,y = coord
    print("x,y:",coord)
    #Limites pour être dans une cellule du labyrinthe (Attention au repère)
    x_origine,y_origine = dicoJeu["origine_graph"]
    x_max = x_origine+dicoJeu["largeur_graph"]
    y_min = y_origine-dicoJeu["hauteur_graph"]

    if x_origine<=x<=x_max and y_min<=y<=y_origine:#Si les coordonnées sont dans le labyrinthe
        x_cellule = abs(x-x_origine)//dicoJeu["epaisseur_cellule"]
        y_cellule = abs(y-y_origine)//dicoJeu["epaisseur_cellule"]
        return(x_cellule,y_cellule)



turtle_flash()
afficheGraphique(dicoJeu)

turtle.done()#garde la fenêtre ouvert