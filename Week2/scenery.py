"""
Joseph Vita
CSCI141 - Herring
9/6/2019

Program uses the turtle graphics framework to draw two facades of
houses and a bubble tree. Program also prints the area of the facades
as well as which one is smallest and largest.
"""

import turtle
import math


def main():
    turtle.setworldcoordinates(-1, -1, 1000, 1000)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    draw_tree(50, 200, 50, 'brown', 'green')
    turtle.forward(150)
    house_length = 100
    big_house_height = 150
    small_house_height = 75
    draw_house(house_length, big_house_height, 50, 'blue', 'orange', 'green', 'yellow')
    turtle.forward(150)
    draw_house(house_length, small_house_height, 50, 'red', 'yellow', 'purple', 'green')
    turtle.forward(150)
    draw_tree(30, 150, 75, 'blue', 'pink')
    print("Bigger house area: ", house_length * big_house_height)
    print("Smaller house area: ", house_length * small_house_height)
    print("Press the [x] button on the top of the window to close")

def draw_triangle(base, height):
    """
    :param base:
    :param height:
    :return: none

    precondition: Turtle is on bottom left side of triangle
    precondition: Turtle is facing east
    postcondition: turtle ends on bottom left
    postcondition: turtle ends with pen down
    postcondition: turtle ends facing down
    """

    turtle.pendown()
    turtle.forward(base)
    angle = math.degrees(math.atan(2 * height / base))
    turtle.left(180 - angle)
    side = math.sqrt((height ** 2) + (base ** 2) / 4)
    turtle.forward(side)
    turtle.left((2 * angle))
    turtle.forward(side)
    turtle.left(angle)


def draw_rectangle(length, height):
    """
        :param length:
        :param height:
        :return: none

        precondition: turtle is on bottom left side of rectangle
        precondition: turtle is facing east
        postcondition: turtle ends with pen down
        postcondition: turtle ends facing down
        postcondition: turtle ends bottom right
    """
    turtle.pendown()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)


def draw_window(size, color):
    """

    :param size:
    :param color:
    :return:

    precondition: turtle facing right
    precondition: pen is up
    postcondition: pen is up
    postcondition:
    """
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    draw_rectangle(size, size)
    turtle.end_fill()
    turtle.penup()


def draw_house(length, height, roof_height, wall_color, roof_color, window_color, door_color):
    """
    :param length:
    :param height:
    :param roof_height:
    :param wall_color:
    :param roof_color:
    :param window_color:
    :return: none

    precondition: Turtle is on bottom left side of house base
    precondition: Turtle is facing east
    precondition: turtle pen is up
    postcondition: turtle ends up on bottom right side of house
    postcondition: turtle is facing east
    postcondition: turtle has pen up
    """
    turtle.pendown()
    turtle.fillcolor(wall_color)
    turtle.begin_fill()
    draw_rectangle(length, height)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    draw_triangle(length, roof_height)
    turtle.end_fill()
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length * 2 // 5)
    turtle.left(90)
    turtle.fillcolor(door_color)
    turtle.begin_fill()
    turtle.forward(height // 3)
    turtle.right(90)
    turtle.forward(length // 6)
    turtle.right(90)
    turtle.forward(height // 3)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward((length // 6) + (length * 2 // 5))
    turtle.left(180)
    turtle.forward(length // 6)
    turtle.left(90)
    turtle.penup()
    turtle.forward(height // 4)
    turtle.right(90)
    draw_window(length // 8, window_color)
    turtle.right(90)
    turtle.forward(height // 4)
    turtle.left(90)
    turtle.forward(length / 2)
    turtle.left(90)
    turtle.forward(height // 4)
    turtle.right(90)
    draw_window(length // 8, window_color)
    turtle.right(90)
    turtle.forward(height // 4)
    turtle.right(90)
    turtle.forward(length // 2 + length // 6)
    turtle.right(180)
    if height >= length:
        turtle.forward(length // 8)
        turtle.left(90)
        turtle.forward(height * 2 / 3)
        turtle.right(90)
        draw_window(length // 8, window_color)
        turtle.forward(length // 3)
        draw_window(length // 8, window_color)
        turtle.forward(length // 3)
        draw_window(length // 8, window_color)
        turtle.right(90)
        turtle.forward(height * 2 / 3)
        turtle.right(90)
        turtle.forward(length // 8 + length // 3 + length // 3)
        turtle.left(180)
    turtle.forward(length)
    turtle.penup()


def draw_tree(length, height, radius, bark_color, leaf_color):
    """

    :param length:
    :param height:
    :param radius:
    :param bark_color:
    :param leaf_color:
    :return:

    precondition: turtle on bottom left
    precondition: turtle facing east
    postcondition: turtle on bottom right
    postcondition: turtle facing east
    postcondition: turtle pen up
    """

    turtle.pendown()
    turtle.fillcolor(bark_color)
    turtle.begin_fill()
    draw_rectangle(length, height)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length // 2)
    turtle.fillcolor(leaf_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.backward(length // 2)
    turtle.right(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.penup()


main()

turtle.done()
