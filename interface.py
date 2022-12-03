import tkinter as tk
from navigation import position_depart,explorer,inverserChemin,suivreChemin,haut,bas,droite,gauche

def map_keys(dicoJeu:dict):
    """Contrôle au clavier pour la turtle"""
    #Correspondance touches
    turtle = dicoJeu["turtle"]
    turtle.onkeypress(lambda : gauche(dicoJeu), "Left")
    turtle.onkeypress(lambda : droite(dicoJeu), "Right")
    turtle.onkeypress(lambda : haut(dicoJeu), "Up")
    turtle.onkeypress(lambda : bas(dicoJeu), "Down")
    turtle.listen()

    #Paramètres turtle rapide
    dicoJeu["turtle"].delay(0)
    dicoJeu["turtle"].speed(0)

def unmap_keys(dicoJeu:dict):
    """Enlève le contrôle manuel de la tortue pour le passage en automatique"""
    #Suppresion des touches
    turtle = dicoJeu["turtle"]
    turtle.onkeypress(None, "Left")
    turtle.onkeypress(None, "Right")
    turtle.onkeypress(None, "Up")
    turtle.onkeypress(None, "Down")

    #On ralenti la turtle
    dicoJeu["turtle"].delay(10)
    dicoJeu["turtle"].speed(1)

def pack_buttons(button_dict:dict):
    """affiche tout les boutons contenus dans button_dict"""
    for b in button_dict.keys():
        button_dict[b].pack(side="left")

def remove_buttons(button_dict:dict):
    """enlève de l'affichage tout les boutons de button_dict"""
    for b in button_dict:
        button_dict[b].pack_forget()

def create_inter(dicoJeu:dict):
    """Créer l'interface de contrôle"""
    #On récupère la fenêtre de turtle
    screen = dicoJeu["turtle"].Screen()
    canvas = screen.getcanvas()
    button_dict = {}
    button_dict["manuel"] = tk.Button(canvas.master, text="Mode manuel", command = lambda : mode_manuel(dicoJeu,button_dict))
    button_dict["exploration_auto"] = tk.Button(canvas.master, text="Exploration auto", command = lambda : exploration_auto(dicoJeu,button_dict,canvas))
    

    pack_buttons(button_dict)


def mode_manuel(dicoJeu:dict,button_dict:dict):
    #On enlève le bouton aller si il existe
    if "aller" in button_dict.keys():
        button_dict["aller"].pack_forget()#on le supprime visuelement
        button_dict.pop("aller")

    map_keys(dicoJeu)#on remet le contrôle manuel

def aller(dicoJeu:dict,button_dict:dict,chemin:list[str],inverser):
    if inverser:
        remove_buttons(button_dict)
        inverserChemin(chemin,dicoJeu)
        button_dict["aller"]["text"] = "aller à la sortie"
        button_dict["aller"]["command"] = lambda : aller(dicoJeu,button_dict,chemin,False)
        pack_buttons(button_dict)
    else:
        remove_buttons(button_dict)
        suivreChemin(chemin,dicoJeu)
        button_dict["aller"]["text"] = "aller à l'entrée"
        button_dict["aller"]["command"] = lambda : aller(dicoJeu,button_dict,chemin,True)
        pack_buttons(button_dict)
7
def chemin_affichage_update(dicoJeu:dict,chemin_affichage:tk.Label,tk_instance:tk.Tk):
    """Met à jour l'affichage du chemin d'exploration"""
    if "chemin_exp" in dicoJeu.keys():
        chemin_affichage["text"] = " ".join(dicoJeu["chemin_tmp"])
    if chemin_affichage.winfo_ismapped():#Si chemin_affichage est visible
        tk_instance.after(100,lambda : chemin_affichage_update(dicoJeu,chemin_affichage,tk_instance))#la fonction s'autoappel dans 100 ms

def exploration_auto(dicoJeu:dict, button_dict:dict, canvas:tk.Canvas,):
    """commande du bouton mode automatique/manuel"""

    position_depart(dicoJeu)
    unmap_keys(dicoJeu)#enlève le contrôle manuel
    
    #On enlève les bouttons
    remove_buttons(button_dict)

    chemin_affichage = tk.Label(canvas.master)
    chemin_affichage.pack(side="left")
    tk_instance = canvas.winfo_toplevel() # récuperation de l'instance tk de turtle
    tk_instance.after(100,lambda : chemin_affichage_update(dicoJeu,chemin_affichage,tk_instance))#appel chemin_affichage_update après 100ms

    chemin = explorer(dicoJeu)

    button_dict["aller"] = tk.Button(canvas.master, text="aller à l'entrée", command = lambda : aller(dicoJeu,button_dict,chemin,True))
    
    chemin_affichage.pack_forget()#On enlève l'affichage du chemin
    #On remet les bouttons
    pack_buttons(button_dict)