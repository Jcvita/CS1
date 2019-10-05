"""
Joseph Vita
CSCI-141 Herring
9/26/19

Python file takes a text file containing lyrics and produces a chart of
colored 10x10 squares that represent the composition of characters in
each word.
"""


import turtle


def main():
    turtle.screensize(800, 800)
    turtle.goto(50, 0)
    draw_square('red')
    turtle.done()


def draw_square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()


main()
