from position import typeCellule

def afficheTextuel(dicoJeu:dict):
    """Affichage textuel du labyrinthe dans dicoJeu, '#'=mur 'x'=entrée 'o'=sortie ' '=passage"""
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])
    #on parcours chaque case du labyrinthe
    for j in range(hauteur):
        for i in range(largeur):
            case = (i,j)
            if laby_liste[j][i] == 1: #la case est un mur
                print('#', end='')
            else: #case == 0, la case est un passage
                if dicoJeu["entrée"] == case:
                    print('x', end='')
                elif dicoJeu["sortie"] == case:
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

def afficheGraphique(dicoJeu:dict,epaisseur_cellule:int=40):
    """Affichage graphique avec turtle du labyrinthe, case blanche=passage, noire=mur, verte=entrée, rouge=sortie
    l'origine correspond au coin supérieur gauche"""
    turtle = dicoJeu["turtle"]
    laby_liste = dicoJeu["laby"]
    hauteur = len(laby_liste)
    largeur = len(laby_liste[0])

    #On place l'origine de manière à centrer le labyrinthe sur la fenêtre
    origine = (-epaisseur_cellule*largeur/2,epaisseur_cellule*hauteur/2)

    #On stock des informations utiles pour d'autres fonctions dépendantes de l'affichage graphique
    dicoJeu["origine_graph"] = origine
    dicoJeu["epaisseur_cellule"] = epaisseur_cellule
    dicoJeu["hauteur"] = hauteur
    dicoJeu["largeur"] = largeur
    dicoJeu["hauteur_graph"] = hauteur*epaisseur_cellule
    dicoJeu["largeur_graph"] = largeur*epaisseur_cellule

    #Paramètres de départ pour la turtle
    turtle.penup()
    turtle.goto(origine)
    turtle.setheading(0)#dirigé vers la droite
    
    #itération de chaque cellule du labyrinthe afin de les dessiner
    for j in range(hauteur):
        for i in range(largeur):
            case = (i,j)
            
            if laby_liste[j][i] == 1:#si la cellule est un mur
                carre(turtle,epaisseur_cellule)
            
            elif case == dicoJeu["entrée"]:#entrée
                carre(turtle,epaisseur_cellule,"green")
            
            elif case == dicoJeu["sortie"]:#sortie
                carre(turtle,epaisseur_cellule,"red")
            
            elif typeCellule(case,dicoJeu) == "carrefour":
                carre(turtle,epaisseur_cellule,"blue")
            
            elif typeCellule(case,dicoJeu) == "impasse":
                carre(turtle,epaisseur_cellule,"orange")
            #si on a juste un passage on effectue seulement le décalage
            turtle.forward(epaisseur_cellule)#Décalage pour passer à la cellule suivante de la ligne
        #Passage à la ligne du dessous
        turtle.goto((origine[0],origine[1]-(1+j)*epaisseur_cellule))
    #Fin du dessin
    turtle.color("black")