import lireLaby


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
