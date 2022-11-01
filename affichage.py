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


def carre(turtle,cote:int,couleur:str="black"):
    """Dessine un carré"""
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

def afficheGraphique(dicoJeu:dict,origine:tuple[float,float]=(-400,400),epaisseur_cellule:int=40):
    """Affichage graphique avec turtle du labyrinthe, case blanche=passage, noire=mur, verte=entrée, rouge=sortie
    l'origine correspond au coin supérieur gauche"""
    turtle = dicoJeu["turtle"]
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])

    #Paramètres de départ pour la turtle
    turtle.penup()
    turtle.goto(origine)
    turtle.setheading(0)#dirigé vers la droite
    
    #itération de chaque cellule du labyrinthe afin de les dessiner
    for j in range(hauteur):
        for i in range(largeur):
            if laby_liste[j][i] == 1:#si la cellule est un mur
                carre(turtle,epaisseur_cellule)
            elif [j,i] == dicoJeu["entrée"]:#entrée
                carre(turtle,epaisseur_cellule,"green")
            elif [j,i] == dicoJeu["sortie"]:#sortie
                carre(turtle,epaisseur_cellule,"red")
            #si on a juste un passage on effectue seulement le décalage
            turtle.forward(epaisseur_cellule)#Décalage pour passer à la cellule suivante de la ligne
        #Passage à la ligne du dessous
        turtle.goto((origine[0],origine[1]-(1+j)*epaisseur_cellule))
    #Fin du dessin
    #On stock des informations utiles pour d'autres fonctions dépendantes de l'affichage graphique
    dicoJeu["origine_graph"] = origine
    dicoJeu["epaisseur_cellule"] = epaisseur_cellule
    dicoJeu["hauteur"] = hauteur
    dicoJeu["largeur"] = largeur
    dicoJeu["hauteur_graph"] = hauteur*epaisseur_cellule
    dicoJeu["largeur_graph"] = largeur*epaisseur_cellule