from random import randint,shuffle
from position import passages_voisins

def solvable(laby:list,depart:tuple[int,int],destination:tuple[int,int],cases_explorées:list=[]):
    """Retourne si un chemin existe entre le départ et la destination dans le labyrinthe (récursif)"""
    if abs(depart[0]-destination[0])+abs(depart[1]-destination[1]) <= 1:#Si on est sur la destination ou à côté alors c'est qu'on a réussi à relier le départ d'origine à la destination
        return True
    else:
        #On explore le ou les chemins voisins non visités
        for v in passages_voisins(depart,laby):
            if v not in cases_explorées:
                cases_explorées.append(v)#On ajoute le voisin aux cases explorées
                if solvable(laby, v, destination, cases_explorées): #On explore le voisin
                    return True
        #Si le chemin échoue
        return False


def random_generate(largeur:int,hauteur:int,entree:tuple[int,int],sortie:tuple[int,int]):
    """génère un labyrinthe aléatoire"""
    assert(entree[0] < largeur and entree[1] < hauteur), "Entrée en dehors du labyrinthe"
    assert(sortie[0] < largeur and sortie[1] < hauteur), "Sortie en dehors du labyrinthe"

    #On créer un labyrinthe sans mur
    laby = []
    for j in range(hauteur):
        laby.append([])
        for i in range(largeur):
            laby[j].append(0)
    
    #On fait une liste de toute les cases du labyrinthe
    cases = []
    for j in range(hauteur):
        for i in range(largeur):
            cases.append((i,j))
    #On enlève l'entrée et la sortie pour être sûr qu'ils restent des passages
    cases.remove(entree)
    cases.remove(sortie)
    #On mélange la liste pour traité les cases dans un ordre aléatoire
    shuffle(cases)
    
    for case_rand in cases:    

        i_rand,j_rand =  case_rand    
        laby[j_rand][i_rand] = 1 #On transforme la case en mur
        #On veut vérifier que le nouveau mur ne créé pas de partie innaccessible
        voisins = passages_voisins(case_rand,laby)
        for i in range(len(voisins)-1):
            if not solvable(laby, voisins[i], voisins[-1],[]):#si il n'existe pas un chemin entre le voisin itéré et le dernier voisin
                laby[j_rand][i_rand] = 0#On annule le mur


    return laby