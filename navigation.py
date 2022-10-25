#!/bin/env python3
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------------------------
navigation.py : déplacement de la tortue / turtle motions

SPDX-FileCopyrightText: 2022 UGA            <carole.adam@univ-grenoble-alpes.fr>
SPDX-License-Identifier: CC-BY-NC-SA-4.0

Voir l'avis de copyright à la fin de ce fichier.
See copyright notice at the end of this file.
--------------------------------------------------------------------------------
"""

# ----- CODE DE navigation.py -----

import turtle as tt


def gauche():
    """
    ...
    """
    print("gauche ; left")


def droite():
    """
    ...
    """
    print("droite ; right")


def bas():
    """
    ...
    """
    print("bas ; down")


def haut():
    """
    ...
    """
    print("haut ; up")


# key bindings
tt.onkeypress(gauche, "Left")
tt.onkeypress(droite, "Right")
tt.onkeypress(haut, "Up")
tt.onkeypress(bas, "Down")
tt.listen()

# start loop
tt.goto(0, 0)
tt.mainloop()
