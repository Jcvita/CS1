"""
Joseph Vita
CSCI-141 Herring
9/27/19

Program takes a user inputted text file of a song and converts the characters
of each line into a colored square based on each character's ascii value.
"""

import turtle


def main():
    lyrics = input("What is the file you want to use")
    lyrics = open(lyrics)
    turtle.speed(0)
    turtle.screensize(800, 800)
    turtle.up()
    turtle.goto(-300, 300)
    turtle.down()
    picture(lyrics)
    turtle.done()


def square(color):
    """
    draw a 10x10 square filled with a given color

    precondition: top left of square facing east pen down
    postcondition: top right of square facing east pen down
    :param color:
    :return:
    """
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


def paint_line(line):
    """
    takes generates a colored square for each char in a given line.
    Square is colored based on the ascii value of that character

    precondition: top left of line facing east
    postcondition: top left of next line facing east(10px down)
    :param line:
    :return:
    """
    for char in line:
        if ord(char) < 70:
            square('red')
        elif ord(char) < 100:
            square('green')
        elif ord(char) < 110:
            square('blue')
        elif ord(char) < 122:
            square('yellow')
        else:
            square('purple')
    turtle.up()
    turtle.right(180)
    for char in line:
        turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)


def picture(file):
    """
    picture draws a line for every line in the given file.

    precondition: paint_line works
    :param file:
    :return:
    """
    for line in file:
        paint_line(line)


if __name__ == '__main__':
    main()
