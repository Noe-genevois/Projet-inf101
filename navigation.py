from position import get_pos_cell,typeCellule

def erreur_mouvement(dicoJeu:dict):
    """Affiche une erreur pour un mouvement impossible, à appeler dans les fonctions de navigation"""
    turtle = dicoJeu["turtle"]
    turtle.color("red")
    print("Erreur, mouvement impossible")

def avancer(dicoJeu:dict):
    """Avance la turtle de une cellule"""
    turtle = dicoJeu["turtle"]
    turtle.forward(dicoJeu["epaisseur_cellule"])

def couleur_turtle_case(i:int,j:int,dicoJeu:dict):
    """Change la couleur de la turtle en fonction du type de la case (i,j)"""
    type_case = typeCellule(i,j,dicoJeu)
    turtle = dicoJeu["turtle"]
    if type_case == "carrefour":
        turtle.color("blue")
    elif type_case == "impasse":
        turtle.color("orange")
    elif type_case == "sortie":
        turtle.color("green")
        print("Victoire, la sortie a été trouvée")
    else:
        turtle.color("black")

def gauche(dicoJeu:dict):
    dicoJeu["commandes"].append('g')#Enregistrement de la commande
    
    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=i-1:#Si la cellule à gauche est dans le labyrinthe
        if dicoJeu["laby"][j][i-1] != 1:#Si la cellule à gauche n'est pas un mur
            turtle.setheading(180)
            avancer(dicoJeu)
            print("gauche ; left")
            couleur_turtle_case(i-1,j,dicoJeu)
            return True
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def droite(dicoJeu:dict):
    dicoJeu["commandes"].append('d')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if i+1<dicoJeu["largeur"]:#Si la cellule à droite est dans le labyrinthe
        if dicoJeu["laby"][j][i+1] != 1:#Si la cellule à droite n'est pas un mur
            turtle.setheading(0)
            avancer(dicoJeu)
            print("droite ; right")
            couleur_turtle_case(i+1,j,dicoJeu)
            return True
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def bas(dicoJeu:dict):
    dicoJeu["commandes"].append('b')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if j+1<dicoJeu["hauteur"]:#Si la cellule en dessous est dans le labyrinthe
        if dicoJeu["laby"][j+1][i] != 1:#Si la cellule en dessous n'est pas un mur
            turtle.setheading(270)
            avancer(dicoJeu)
            print("bas ; down")
            couleur_turtle_case(i,j+1,dicoJeu)
            return True
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def haut(dicoJeu:dict):
    dicoJeu["commandes"].append('h')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=j-1:#Si la cellule au dessus est dans le labyrinthe
        if dicoJeu["laby"][j-1][i] != 1:#Si la cellule au dessus n'est pas un mur
            turtle.setheading(90)
            avancer(dicoJeu)
            print("haut ; up")
            couleur_turtle_case(i,j-1,dicoJeu)
            return True
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def suivreChemin(li:list[str],dicoJeu:dict):
    """Execute le chemin li (liste de 'g','d','h','b') avec la turtle"""
    for i in range(len(li)):#On parcours li
        cmd = li[i]
        #On effectue le mouvement
        if cmd == 'g':
            mvt = gauche(dicoJeu)
        elif cmd == 'd':
            mvt = droite(dicoJeu)
        elif cmd == 'b':
            mvt = bas(dicoJeu)
        elif cmd == "h":
            mvt = haut(dicoJeu)
        else:#Si on a une commande inconnue dans li
            print("Erreur, commande invalide")
            return
        if not mvt:#Si la commande a raté
            print("Erreur, chemin impossible")
            return
    
    print("Chemin effectué")

def inverserChemin(li:list[str],dicoJeu:dict):
    """Execute le chemin li (liste de 'g','d','h','b') avec la turtle en sens inverse"""
    for i in range(len(li)-1,-1,-1):#On parcours li en sens inverse
        cmd = li[i]
        #On effectue le mouvement
        if cmd == 'd':
            mvt = gauche(dicoJeu)
        elif cmd == 'g':
            mvt = droite(dicoJeu)
        elif cmd == 'h':
            mvt = bas(dicoJeu)
        elif cmd == "b":
            mvt = haut(dicoJeu)
        else:#Si on a une commande inconnue dans li
            print("Erreur, commande invalide")
            return
        if not mvt:#Si la commande a raté
            print("Erreur, chemin impossible")
            return
    
    print("Chemin effectué")