"""
Joseph Vita
8/26/19
CS-141 Herring

hexes.py uses turtle to draw 2 large hexagons that are comprised of smaller hexagons. The second hexagon is offset by
the same distance as one side of a hexagon.
"""

import turtle


def makeHex():
    """generates a hexagon by moving forward 50 pixels 6 times with a difference of 60 degrees each"""

    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)


def makeBigHex():
    """Uses makeHex() 6 times at 60 degree intervals to make a larger hexagon out of smaller hexagons"""

    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()
    turtle.forward(50)
    turtle.right(60)
    makeHex()


makeBigHex()
turtle.right(60)
makeBigHex()

turtle.done()
