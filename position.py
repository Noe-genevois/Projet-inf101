def pixel2cell(x:float,y:float, dicoJeu:dict):
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

def typeCellule(coord:tuple[int,int],dicoJeu:dict):
    """Donne le type de la cellule (entrée,sortie,mur,passage,impasse,carrefour) pour la cellule aux coordonnées i,j"""
    i,j = coord
    if not(0<=i<dicoJeu["largeur"] and 0<=j<dicoJeu["hauteur"]): #Si la case est en dehors du labyrinthe
        return None
    else:

        if dicoJeu["entrée"] == coord:
            return "entrée"
        elif dicoJeu["sortie"] == coord:
            return "sortie"
        else:
            cellule = dicoJeu["laby"][j][i]
            if cellule == 1:
                return "mur"
            elif cellule == 0:#la cellule est un passage
                #On veut compter le nombre de voisins(dessus,dessous,droite et gauche) qui sont des passages
                nbr_passage_voisin = len(passages_voisins(coord,dicoJeu["laby"]))
                
                if nbr_passage_voisin == 1:
                    return "impasse"
                elif nbr_passage_voisin == 2:
                    return "passage"
                elif nbr_passage_voisin > 2:
                    return "carrefour"
        
def testClic(x:float,y:float,dicoJeu:dict):
    """Donne la position et le type d'une cellule à une position x,y"""
    cell = pixel2cell(x,y,dicoJeu)
    if cell != None:#Si on est dans le labyrinthe
        i,j = cell
        print("Ligne:",j," Colonne:",i)
        print("Type:",typeCellule(cell,dicoJeu))#amélioration pour tester typeCellule
    else:
        print("Erreur, en dehors du labyrinthe")

def get_pos_cell(dicoJeu:dict):
    """Renvoi la cellule où se trouve la turtle"""
    return pixel2cell(dicoJeu["turtle"].xcor(),dicoJeu["turtle"].ycor(),dicoJeu)

def passages_voisins(case:tuple[int,int], laby:list):
    """retourne les coordonnées des passages voisins d'une case"""
    i,j = case
    voisins = []
    for i_voisin,j_voisin in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:#itération de toutes les cases voisines
        if 0<=j_voisin<len(laby) and 0<=i_voisin<len(laby[0]):#Si le voisin existe dans le labyritnhe
            if laby[j_voisin][i_voisin] == 0:#Si c'est un passage
                voisins.append((i_voisin,j_voisin))
    return voisins