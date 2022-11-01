from position import pixel2cell,get_pos_cell

def erreur_mouvement(dicoJeu:dict):
    """Affiche une erreur pour un mouvement impossible, à appeler dans les fonctions de navigation"""
    turtle = dicoJeu["turtle"]
    turtle.color("red")
    print("Erreur, mouvement impossible")

def avancer(dicoJeu:dict):
    """Avance la turtle de une cellule"""
    turtle = dicoJeu["turtle"]
    turtle.forward(dicoJeu["epaisseur_cellule"])

def test_victoire(i:int,j:int,dicoJeu:dict):
    """Test si la turtle est sur la sortie et affiche la victoire si nécessaire"""
    turtle = dicoJeu["turtle"]
    if [j,i] == dicoJeu["sortie"]:
        print("Victoire, la sortie a été trouvée")
        turtle.color("green")

def gauche(dicoJeu:dict):
    turtle = dicoJeu["turtle"]
    turtle.color(dicoJeu["couleur_turtle"])#Couleur par défaut de la turtle pour qu'elle ne reste pas rouge après une erreur
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=i-1:#Si la cellule à gauche est dans le labyrinthe
        if dicoJeu["laby"][j][i-1] != 1:#Si la cellule à gauche n'est pas un mur
            turtle.setheading(180)
            avancer(dicoJeu)
            print("gauche ; left")
            test_victoire(i-1,j,dicoJeu)
            return
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)

def droite(dicoJeu:dict):
    turtle = dicoJeu["turtle"]
    turtle.color(dicoJeu["couleur_turtle"])#Couleur par défaut de la turtle pour qu'elle ne reste pas rouge après une erreur
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if i+1<dicoJeu["largeur"]:#Si la cellule à droite est dans le labyrinthe
        if dicoJeu["laby"][j][i+1] != 1:#Si la cellule à droite n'est pas un mur
            turtle.setheading(0)
            avancer(dicoJeu)
            print("droite ; right")
            test_victoire(i+1,j,dicoJeu)
            return
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)


def bas(dicoJeu:dict):
    turtle = dicoJeu["turtle"]
    turtle.color(dicoJeu["couleur_turtle"])#Couleur par défaut de la turtle pour qu'elle ne reste pas rouge après une erreur
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if j+1<dicoJeu["hauteur"]:#Si la cellule en dessous est dans le labyrinthe
        if dicoJeu["laby"][j+1][i] != 1:#Si la cellule en dessous n'est pas un mur
            turtle.setheading(270)
            avancer(dicoJeu)
            print("bas ; down")
            test_victoire(i,j+1,dicoJeu)
            return
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)


def haut(dicoJeu:dict):
    turtle = dicoJeu["turtle"]
    turtle.color(dicoJeu["couleur_turtle"])#Couleur par défaut de la turtle pour qu'elle ne reste pas rouge après une erreur
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=j-1:#Si la cellule au dessus est dans le labyrinthe
        if dicoJeu["laby"][j-1][i] != 1:#Si la cellule au dessus n'est pas un mur
            turtle.setheading(90)
            avancer(dicoJeu)
            print("haut ; up")
            test_victoire(i,j-1,dicoJeu)
            return
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement()