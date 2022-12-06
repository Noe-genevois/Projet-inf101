from random import randint


def solvable(laby:list,depart,destination,explore=[]):
    """Retourne si un chemin existe entre le départ et la destination dans le labyrinthe (récursif)"""
    if abs(depart[0]-destination[0])+abs(depart[1]-destination[1]) <= 1:#Si on est sur la destination ou à côté alors c'est qu'on a réussi à relier le départ d'origine à la destination
        return True
    else:
        #On prend tout les passage voisin que l'on a pas visité
        j,i = depart
        passages_voisins = []
        for j_voisin,i_voisin in [[j-1,i],[j,i+1],[j+1,i],[j,i-1]]:
            if 0<=j_voisin<len(laby) and 0<=i_voisin<len(laby[0]):#si le voisin est dans le labyrinthe
                if [j_voisin,i_voisin] not in explore:#si on ne l'a pas exploré
                    if laby[j_voisin][i_voisin] == 0:#si c'est un passage
                        passages_voisins.append([j_voisin,i_voisin])

        #On explore le ou les chemins voisins
    
        for i in range(len(passages_voisins)):#Exploration de tout les chemins voisins
            explore+=[passages_voisins[i]]#On ajoute la case voisine aux cases explorées
            if solvable(laby,passages_voisins[i],destination,explore):#On l'explore
                return True
        #Si on échoue à trouver un chemin
        return False


def nbr_murs(laby):
    """Renvoi le nombre de murs d'un labyrinthe"""
    n = 0
    for l in laby:
        n += sum(l)
    return n


def random_generate(largeur:int,hauteur:int,entree,sortie):
    """génère un labyrinthe aléatoire"""
    #On créer un labyrinthe sans mur
    laby = []
    for j in range(hauteur):
        laby.append([])
        for i in range(largeur):
            laby[j].append(0)
    
    nbr_max_murs = largeur*hauteur//2
    wall_already_tried = []

    #Dans cette partie on prend des cases au hasard pour les transformer en mur en s'assurant de la viabilité du labyritnhe
    while nbr_murs(laby) < nbr_max_murs and len(wall_already_tried) <= largeur*hauteur-2: #Tant qu'on a pas atteint le nombre de murs désiré et qu'on a encore des murs à essayer       
        
        #Case aléatoire
        j_rand = randint(0,hauteur-1)
        i_rand = randint(0,largeur-1)

        #Si la coordonnée a pas déjà été itérée et que ce n'est ni l'entrée ni la sortie
        if [j_rand,i_rand] not in wall_already_tried and [j_rand,i_rand] != entree and [j_rand,i_rand] != sortie:        
            laby[j_rand][i_rand] = 1 #On transforme la case en mur
            wall_already_tried.append([j_rand,i_rand])#On ajoute la case au murs qu'on a déjà au moins essayé
            #On itère les voisin pour vérifier que le nouveau mur ne créé pas de partie inaccessible
            for voisin in [[j_rand-1,i_rand],[j_rand+1,i_rand],[j_rand,i_rand+1],[j_rand,i_rand-1]]:
                j_voisin,i_voisin = voisin
                if 0<=j_voisin<len(laby) and 0<=i_voisin<len(laby[0]):
                    if laby[j_voisin][i_voisin] == 0:
                        if not solvable(laby, entree, voisin, explore=[]):#Si on ne peu plus atteindre ce voisin
                            laby[j_rand][i_rand] = 0#On annule le mur
    
    return laby