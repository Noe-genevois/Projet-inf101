#!/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
lireLaby.py : lecture de labyrinthes / Maze input

SPDX-FileCopyrightText: 2022 UGA            <carole.adam@univ-grenoble-alpes.fr>
SPDX-License-Identifier: CC-BY-NC-SA-4.0

Voir l'avis de copyright à la fin de ce fichier.
See copyright notice at the end of this file.
--------------------------------------------------------------------------------
"""

def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
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
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut