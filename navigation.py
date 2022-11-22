from position import get_pos_cell,typeCellule

def erreur_mouvement(dicoJeu:dict):
    """Affiche une erreur pour un mouvement impossible, à appeler dans les fonctions de navigation"""
    turtle = dicoJeu["turtle"]
    turtle.color("red")
    print("Erreur, mouvement impossible")

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

def avancer(dicoJeu:dict):
    """Avance la turtle de une cellule"""
    turtle = dicoJeu["turtle"]
    turtle.forward(dicoJeu["epaisseur_cellule"])

def gauche(dicoJeu:dict):
    dicoJeu["chemin"].append('g')#Enregistrement de la commande
    
    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=i-1:#Si la cellule à gauche est dans le labyrinthe
        if dicoJeu["laby"][j][i-1] != 1:#Si la cellule à gauche n'est pas un mur
            turtle.setheading(180)
            avancer(dicoJeu)
            print("gauche ; left")
            couleur_turtle_case(i-1,j,dicoJeu)#Changement couleur turtle
            return True#commande réussie
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def droite(dicoJeu:dict):
    dicoJeu["chemin"].append('d')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if i+1<dicoJeu["largeur"]:#Si la cellule à droite est dans le labyrinthe
        if dicoJeu["laby"][j][i+1] != 1:#Si la cellule à droite n'est pas un mur
            turtle.setheading(0)
            avancer(dicoJeu)
            print("droite ; right")
            couleur_turtle_case(i+1,j,dicoJeu)#Changement couleur turtle
            return True#commande réussie
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def bas(dicoJeu:dict):
    dicoJeu["chemin"].append('b')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if j+1<dicoJeu["hauteur"]:#Si la cellule en dessous est dans le labyrinthe
        if dicoJeu["laby"][j+1][i] != 1:#Si la cellule en dessous n'est pas un mur
            turtle.setheading(270)
            avancer(dicoJeu)
            print("bas ; down")
            couleur_turtle_case(i,j+1,dicoJeu)#Changement couleur turtle
            return True#commande réussie
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def haut(dicoJeu:dict):
    dicoJeu["chemin"].append('h')#Enregistrement de la commande

    turtle = dicoJeu["turtle"]
    i,j = get_pos_cell(dicoJeu) #cellule où se trouve la turtle
    if 0<=j-1:#Si la cellule au dessus est dans le labyrinthe
        if dicoJeu["laby"][j-1][i] != 1:#Si la cellule au dessus n'est pas un mur
            turtle.setheading(90)
            avancer(dicoJeu)
            print("haut ; up")
            couleur_turtle_case(i,j-1,dicoJeu)#Changement couleur turtle
            return True#commande réussie
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
    """Execute le chemin li (liste de 'g','d','h','b') avec la turtle, en sens inverse"""
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
            print("Erreur, commande inconnue")
            return
        if not mvt:#Si la commande a raté
            print("Erreur, chemin impossible")
            return
    
    print("Chemin effectué")


def explorer(dicoJeu:dict):
    """Exploration automatique du labyrinthe avec la turtle"""
    i,j = get_pos_cell(dicoJeu)
    positions_explorées = []
    chemin = []
    commandes_inversées = {'h':bas,'b':haut,'g':droite,'d':gauche}
    
    while typeCellule(i,j,dicoJeu) != "sortie":
        positions_explorées.append((i,j))
        
        commandes = {(i-1,j):(gauche,'g'),(i+1,j):(droite,'d'),(i,j-1):(haut,'h'),(i,j+1):(bas,'b')}#Dictionnaire des voisins, déplacements hypothétique
        commandes_possibles = [] #liste des commandes possibles et qui ne nous ramènent pas en arrière
        for i_dep,j_dep in commandes.keys():#On test toute les nouvelles positions possibles
            if 0<=i_dep<dicoJeu["largeur"] and 0<=j_dep<dicoJeu["hauteur"]:#si la case est dans le labyrinthe
                if typeCellule(i_dep,j_dep,dicoJeu) != "mur":#si la n'est pas un mur
                    if (i_dep,j_dep) not in positions_explorées:#si on est pas déjà allé sur la case
                        commandes_possibles.append(commandes[(i_dep,j_dep)])
        
        if len(commandes_possibles) > 0:#Si il y a une commande possible
            commandes_possibles[0][0](dicoJeu) #On effectue la 1ere commande possible
            chemin.append(commandes_possibles[0][1])#On l'enregistre
            i,j = get_pos_cell(dicoJeu)#on defini la nouvelle position
        else:#Si on a aucune commande possible
            #On retourne au dernier carrefour    
            commandes_inversées[chemin[-1]](dicoJeu)
            chemin.pop(-1)
            i,j = get_pos_cell(dicoJeu)
            while typeCellule(i,j,dicoJeu) != "carrefour":
                commandes_inversées[chemin[-1]](dicoJeu)
                chemin.pop(-1)
                i,j = get_pos_cell(dicoJeu)
    
    return chemin



