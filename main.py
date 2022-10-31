from numpy import double
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
    for j in range(hauteur):
        for i in range(largeur):
            if laby_liste[j][i] == 1:#si la cellule est un mur
                carre(epaisseur_cellule)
            elif [j,i] == dicoJeu["entrée"]:#entrée
                carre(epaisseur_cellule,"green")
            elif [j,i] == dicoJeu["sortie"]:#sortie
                carre(epaisseur_cellule,"red")
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

#--------------------- Positionnement de la tortue ---------------------
def pixel2cell(x:double,y:double, dicoJeu:dict):
    """Conversion de coordonnées turtle en coordonnées dans le labyrinthe, return None si on est en dehors du labyrinthe"""
    #Limites pour être dans une cellule du labyrinthe (Attention au repère)
    x_origine,y_origine = dicoJeu["origine_graph"]
    x_max = x_origine+dicoJeu["largeur_graph"]
    y_min = y_origine-dicoJeu["hauteur_graph"]

    if x_origine<=x<=x_max and y_min<=y<=y_origine:#Si les coordonnées sont dans le labyrinthe
        i = int(abs(x-x_origine)//dicoJeu["epaisseur_cellule"])
        j = int(abs(y-y_origine)//dicoJeu["epaisseur_cellule"])
        return(i,j)

def cell2pixel(i:int,j:int,dicoJeu:dict):
    """Conversion de coordonnées du labyrinthe en coordonnées turtle"""
    x_origine,y_origine = dicoJeu["origine_graph"]
    x = x_origine+(i+0.5)*dicoJeu["epaisseur_cellule"]
    y = y_origine-(j+0.5)*dicoJeu["epaisseur_cellule"]
    return (x,y)

def typeCellule(i:int,j:int,dicoJeu:dict):
    """Donne le type de la cellule (entrée,sortie,mur,passage,impasse,carrefour) pour la cellule aux coordonnées i,j"""
    if dicoJeu["entrée"] == [j,i]:
        return "entrée"
    if dicoJeu["sortie"] == [j,i]:
        return "sortie"
    cellule = dicoJeu["laby"][j][i]
    if cellule == 1:
        return "mur"
    if cellule == 0:
        #On veut compter le nombre de voisins(dessus,dessous,droite et gauche) qui sont des passages
        nbr_passage_voisin = 0
        #itération de tout les voisins directs
        for j_voisin in range(j-1,j+2):
            for i_voisin in [[i],[i-1,i+1],[i]][j_voisin-(j-1)]:
                if 0<=j_voisin<dicoJeu["hauteur"] and 0<=i_voisin<dicoJeu["largeur"]:#si le voisin existe bien dans le labyrinthe
                    if dicoJeu["laby"][j_voisin][i_voisin] == 0:
                        nbr_passage_voisin+=1
        
        if nbr_passage_voisin == 1:
            return "impasse"
        if nbr_passage_voisin == 2:
            return "passage"
        return "carrefour" #si on a ni une impasse ni un passage alors c'est un carrefour
                


def testClic(x:double,y:double,dicoJeu:dict):
    cell = pixel2cell(x,y,dicoJeu)
    if cell != None:
        i,j = cell
        print("Ligne:",j," Colonne:",i)
        print("Type:",typeCellule(i,j,dicoJeu))#amélioration pour tester typeCellule
    else:
        print("Erreur, clique en dehors du labyrinthe")

afficheTextuel(dicoJeu)
turtle_flash()
afficheGraphique(dicoJeu)
turtle.onscreenclick(lambda x,y: testClic(x,y,dicoJeu))
turtle.color("green")

turtle.mainloop()