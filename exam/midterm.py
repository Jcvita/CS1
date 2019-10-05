"""
Jospeph Vita
CSCI-141 Herring
10/4/2019

Exam 1
"""

import turtle
import random


def main():
    init()
    # draw_circles(200, 25)
    # draw_color_circles(200, 25, 200, 255, 200)
    draw_spheres(5)
    turtle.done()


def init():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.fillcolor(255, 255, 255)
    turtle.hideturtle()


def draw_circles(rad, dec):
    if rad > 0:
        turtle.circle(rad)
        draw_circles(rad - dec, dec)
    else:
        return 0


def draw_color_circles(rad, dec, r, g, b):
    if rad > 0:
        turtle.fillcolor(r - rad, g - rad, b - rad)
        turtle.begin_fill()
        turtle.color(r - rad, g - rad, b - rad)
        turtle.circle(rad)
        turtle.end_fill()
        draw_color_circles(rad - dec, dec, r, g, b)
    else:
        turtle.color(0, 0, 0)
        return 0


def draw_sphere(rad, dec, r, g, b):
    if rad > 0:
        turtle.fillcolor(r, g, b)
        turtle.begin_fill()
        turtle.color(r - rad, g - rad, b - rad)
        turtle.circle(rad)
        turtle.end_fill()
        turtle.left(90)
        turtle.forward(dec * 1.35) 
        turtle.right(90)
        turtle.forward(dec * .3)
        draw_sphere(rad - dec, dec, r, g, b)
    else:
        return 0


def draw_spheres(num_spheres):
    turtle.right(180)
    turtle.forward(300)
    turtle.right(180)
    for x in range(num_spheres):
        rad = random.randint(30, 75)
        right = random.randint(rad, 600 - rad)
        down = random.randint(rad, 600 - rad)
        rad = random.randint(30, 75)
        turtle.up()
        turtle.forward(right)
        turtle.right(90)
        turtle.forward(down)
        turtle.left(90)
        turtle.down()
        draw_sphere(rad, 5, random.randint(rad, 255), random.randint(rad, 255), random.randint(rad, 255))
        turtle.up()
        turtle.left(90)
        turtle.forward(right)
        turtle.left(90)
        turtle.forward(down)
        turtle.right(180)
        turtle.down()


if __name__ == '__main__':
    main()

