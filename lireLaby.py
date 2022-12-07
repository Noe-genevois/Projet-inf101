from os.path import exists

chemin_dossier_laby = "laby/"

def labyFromFile(fn:str) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    """
    global chemin_dossier_laby
    f = open(chemin_dossier_laby+fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = (inditem,indline)
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = (inditem,indline)
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut

def fichier_existe(fn:str):
    """Renvoi un booléan indiquant si le fichier de labyrinthe existe"""
    global chemin_dossier_laby
    return exists(chemin_dossier_laby+fn)