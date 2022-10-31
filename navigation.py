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

import turtle


def gauche():
    turtle.setheading(180)
    turtle.forward(100)
    print("gauche ; left")


def droite():
    turtle.setheading(0)
    turtle.forward(100)
    print("droite ; right")


def bas():
    turtle.setheading(270)
    turtle.forward(100)
    print("bas ; down")


def haut():
    turtle.setheading(90)
    turtle.forward(100)
    print("haut ; up")


# key bindings
turtle.onkeypress(gauche, "Left")
turtle.onkeypress(droite, "Right")
turtle.onkeypress(haut, "Up")
turtle.onkeypress(bas, "Down")
turtle.listen()

# start loop
turtle.goto(0, 0)
turtle.penup()
turtle.mainloop()
