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


def main():
    turtle.tracer(0, 0)
    # turtle.speed(10)
    turtle.screensize(800, 600)
    # drip = int(input("How many raindrops should there be (1-100)? "))
    # if drip > 100 or drip < 1:
    #     print("Bruh moment! You can only have in between 1 and 100 raindrops.")
    #     exit()
    draw_pond()
    make_it_rain(100)
    turtle.done()


def draw_pond():
    """
    precondition:pen facing east
    precondition:turtle up or down
    postcondition:turtle at top left of pond
    postcondition:turtle up
    :return:
    """
    turtle.fillcolor('lightblue')
    turtle.begin_fill()
    turtle.up()
    turtle.forward(600)
    turtle.left(90)
    turtle.down()
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(1200)
    turtle.left(90)
    turtle.forward(1000)
    turtle.left(90)
    turtle.forward(1200)
    turtle.left(90)
    turtle.forward(1000)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(1200)
    turtle.right(180)


def make_it_rain(drops, accum=0):
    if accum < drops:
        diam = random.randint(1, 20)
        draw_drop(random.randint(diam, 1200 - diam),
                  random.randint(int(diam * 1.5), 1000 - diam),
                  diam)
        make_it_rain(drops, accum + 1)
    else:
        return 0


def draw_drop(x, y, diam):
    """
    Function draws a droplet of a random diameter at the given(random)
    coordinates

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
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(diam)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(y + diam // 2)
    turtle.left(90)
    turtle.forward(x)
    turtle.right(180)

# def draw_ripples(max, x, y):


main()
