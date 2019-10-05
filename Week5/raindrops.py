"""
Joseph Vita
9/23/19
CSCI-141 Herring
Python program draws a lake as well as random raindrops falling on the lake.
Each rain drop creates a number of ripples that are not allowed to go past
the bounds of the lake.
"""
import turtle
import random
import math

LWIDTH = 700
LHEIGHT = 600


def main():
    # turtle.tracer(0, 0)
    turtle.speed(20)
    turtle.screensize(800, 600)
    turtle.colormode(255)
    # drip = int(input("How many raindrops should there be (1-100)? "))
    # if drip > 100 or drip < 1:
    #     print("Bruh moment! You can only have in between 1 and 100 raindrops.")
    #     exit()
    draw_pond()
    make_it_rain(100)

    turtle.done()


def draw_pond():
    """
    Draws and colors the pond area.

    precondition:pen facing east
    precondition:turtle up or down
    postcondition:turtle at top left of pond
    postcondition:turtle up
    :return:
    """
    turtle.fillcolor('lightblue')
    turtle.begin_fill()
    turtle.up()
    turtle.forward(LWIDTH // 2)
    turtle.left(90)
    turtle.down()
    turtle.forward(LHEIGHT // 2)
    turtle.left(90)
    turtle.forward(LWIDTH)
    turtle.left(90)
    turtle.forward(LHEIGHT)
    turtle.left(90)
    turtle.forward(LWIDTH)
    turtle.left(90)
    turtle.forward(LHEIGHT)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(LWIDTH)
    turtle.right(180)


def make_it_rain(drops, accum=0):
    if accum < drops:
        diam = random.randint(1, 20)
        draw_drop(random.randint(diam, LWIDTH - diam),
                  random.randint(int(diam * 1.5), LHEIGHT - diam),
                  diam,
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        make_it_rain(drops, accum + 1)
    else:
        return


def draw_drop(x, y, diam, color):
    """
    Function draws a droplet of a random diameter at the given(random)
    coordinates
    :param color:
    :param x:
    :param y:
    :param diam:
    :return:
    precondition: turtle up or down
    precondition: turtle on top left of screen
    precondition: turtle facing east
    postcondition: same as all preconditions
    """

    turtle.up()
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y + diam // 2)
    turtle.left(90)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(diam)
    turtle.end_fill()
    draw_ripples(random.randint(3, 8), diam, x, y)
    return math.pi * diam


def draw_ripples(ripples, initdiam, x, y):
    """
    precondition:turtle facing east
    precondition:turtle located at the start of the ripple draw spot
    :param initdiam: 
    :param ripples:
    :param x:
    :param y:
    :return:
    """''
    count = 0
    diam = initdiam
    # turtle.right(90)
    nextl = x - diam
    nextr = x + diam
    nextt = y - diam
    nextb = y + diam

<<<<<<< HEAD:Week5/raindrop.py
=======
    while (count < ripples and
            nextt >= 0 and
            nextb <= 600 and
            nextr <= 700 and
            nextl >= 0):
        diam += initdiam // 2
        turtle.up()
        turtle.right(90)
        turtle.forward(initdiam // 2)
        turtle.left(90)
        turtle.down()
        turtle.circle(diam)
        turtle.up()
        nextt -= initdiam // 2
        nextb += initdiam // 2
        nextl -= initdiam // 2
        nextr += initdiam // 2
        count += 1
    turtle.setpos(-350, 300)
>>>>>>> 56d6615e6d915a5dc11745a77ab75244a55b5225:Week5/raindrops.py

def draw_ripples(max, x, y):
    print('yeet')

main()