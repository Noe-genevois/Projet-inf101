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
        for i_voisin,j_voisin in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=j_voisin<dicoJeu["hauteur"] and 0<=i_voisin<dicoJeu["largeur"]:#si le voisin existe bien dans le labyrinthe
                if dicoJeu["laby"][j_voisin][i_voisin] == 0:#Si le voisine est un passage
                    nbr_passage_voisin+=1
        
        if nbr_passage_voisin == 1:
            return "impasse"
        if nbr_passage_voisin == 2:
            return "passage"
        return "carrefour" #si on a ni une impasse ni un passage alors c'est un 
        
def testClic(x:float,y:float,dicoJeu:dict):
    """Donne la position et le type d'une cellule à une position x,y"""
    cell = pixel2cell(x,y,dicoJeu)
    if cell != None:#Si on est dans le labyrinthe
        i,j = cell
        print("Ligne:",j," Colonne:",i)
        print("Type:",typeCellule(i,j,dicoJeu))#amélioration pour tester typeCellule
    else:
        print("Erreur, en dehors du labyrinthe")

def get_pos_cell(dicoJeu:dict):
    """Renvoi la cellule où se trouve la turtle"""
    return pixel2cell(dicoJeu["turtle"].xcor(),dicoJeu["turtle"].ycor(),dicoJeu)