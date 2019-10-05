import turtle


def main():
    """
        Main function sets up the turtle and then calls make_triangle
    """
    depth = int(input("How many layers of depth do you want?"))
    turtle.left(120)
    make_triangle(300, depth)
    turtle.left(150)
    turtle.done()


def make_triangle(size, layers):
    """
        param: size
        param: layers

        precondition: pen is down
    """

    if layers <= 0:
        return 0
    else:
        layers = layers - 1
        turtle.forward(size)
        make_triangle(size // 2, layers)
        turtle.right(120)
        turtle.forward(size)
        turtle.left(120)
        make_triangle(size // 2, layers)
        turtle.right(240)
        turtle.forward(size)
        turtle.right(120)


main()
