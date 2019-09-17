"""
Joseph Vita

Program creates a colored zig zag stair shape using recursion
"""
import turtle


def main():
    turtle.speed(0)
    depth = int(input("How many layers do you want? "))
    zigzag(100, depth, 0)
    turtle.done()


def draw_l(size, back, count):
    """
    param: size

    precondition: turtle facing direction that L should be (north or south)
    precondition: turtle up or down
    postcondition: turtle facing starting direction
    postcondition: turtle up
    """
    if count % 2 == 1:
        turtle.left(45)
    if back == 1:
        turtle.forward(size / 2)
        turtle.right(90)
        turtle.forward(size)
    else:
        turtle.backward(size)
        turtle.left(90)
        turtle.backward(size / 2)
    if count % 2 == 1:
        turtle.right(45)
    turtle.penup()


def zigzag(size, depth, count):
    """
    param: size
    param: depth

    precondition: turtle facing east
    precondition: pen down
    postcondition: turtle facing east
    postcondition: pen up
    """
    turtle.penup()
    if depth < 1:
        pass
    elif depth >= 1:
        turtle.left(90)
        turtle.pendown()
        if count % 2 == 0:
            turtle.pencolor("red")
        else:
            turtle.pencolor("green")
        draw_l(size, 1, count)
        zigzag(size / 2, depth - 1, count + 1)
        turtle.penup()
        draw_l(size, 0, count)
        turtle.right(180)
        turtle.pendown()
        if count % 2 == 0:

            turtle.pencolor("red")
        else:
            turtle.pencolor("green")
        draw_l(size, 1, count)
        zigzag(size / 2, depth - 1, count + 1)
        turtle.penup
        draw_l(size, 0, count)
        turtle.left(90)
        print(count)


main()
