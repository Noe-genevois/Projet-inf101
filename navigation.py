from position import get_pos_cell,typeCellule,cell2pixel,passages_voisins

def position_depart(dicoJeu:dict):
    """Met la tortue à sa position de départ, sûr l'entrée"""
    i_entree,j_entree = dicoJeu["entrée"]
    dicoJeu["turtle"].goto(cell2pixel(i_entree,j_entree,dicoJeu))

def erreur_mouvement(dicoJeu:dict):
    """Affiche une erreur pour un mouvement impossible, à appeler dans les fonctions de navigation"""
    turtle = dicoJeu["turtle"]
    turtle.color("red")
    print("Erreur, mouvement impossible")

def couleur_turtle_case(i:int,j:int,dicoJeu:dict):
    """Change la couleur de la turtle en fonction du type de la case (i,j), affichage du message de victoire"""
    type_case = typeCellule((i,j),dicoJeu)
    turtle = dicoJeu["turtle"]
    if type_case == "carrefour":
        turtle.color("orange")
    elif type_case == "impasse":
        turtle.color("blue")
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
            print("gauche")
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
            print("droite")
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
            print("bas")
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
            print("haut")
            couleur_turtle_case(i,j-1,dicoJeu)#Changement couleur turtle
            return True#commande réussie
    #Si on a pas pu effectuer le mouvement
    erreur_mouvement(dicoJeu)
    return False

def suivreChemin(chemin:list[str],dicoJeu:dict):
    """Execute le chemin (liste de 'g','d','h','b') avec la turtle"""
    for i in range(len(chemin)):#On parcours li
        cmd = chemin[i]
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
            print("Erreur, commande inconnue")
            return
        if not mvt:#Si la commande a raté
            print("Erreur, chemin impossible")
            return
    
    print("Chemin effectué")

def inverserChemin(chemin:list[str],dicoJeu:dict):
    """Execute le chemin li (liste de 'g','d','h','b') avec la turtle, en sens inverse"""
    for i in range(len(chemin)-1,-1,-1):#On parcours li en sens inverse
        cmd = chemin[i]
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
    positions_explorées = []
    chemin = []
    commandes_inversées = {'h':bas,'b':haut,'g':droite,'d':gauche}
    commandes_str = {gauche:'g',droite:'d',haut:'h',bas:'b'}

    while typeCellule(get_pos_cell(dicoJeu),dicoJeu) != "sortie":
        i,j = get_pos_cell(dicoJeu)
        positions_explorées.append((i,j))
        voisins_commandes = {(i-1,j):gauche,(i+1,j):droite,(i,j+1):bas,(i,j-1):haut}#Dictionnaire des cellulees voisines avec la commande pour y aller associée
        
        commande = None #Commande qu'on doit exécuter pour continuer l'exploration
        for coord_voisin in passages_voisins((i,j),dicoJeu["laby"]):#On test toute les nouvelles positions possibles
            if coord_voisin not in positions_explorées:#si on est pas déjà allé sur la case
                    commande = voisins_commandes[coord_voisin]
                    break #On a besoin que d'une seule commande
        
        if commande != None :#Si il y a une commande possible
            commande(dicoJeu) #On execute le mouvement
            chemin.append(commandes_str[commande])#On l'enregistre
        else:#Si on a aucune commande possible
            #On retourne au dernier carrefour
            retour_arriere = True
            while retour_arriere:
                #On dépile la dernière commande executée et on execute son inverse
                commandes_inversées[chemin[-1]](dicoJeu)
                chemin.pop(-1)
                #Si on est revenu à un carrefour ou si on a plus de chemin à remonter
                if typeCellule(get_pos_cell(dicoJeu),dicoJeu) == "carrefour" or len(chemin) == 0:#Condition d'arrêt de la boucle
                    retour_arriere = False
    
    return chemin

