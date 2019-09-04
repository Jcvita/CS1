
import turtle

def init():
    """Initialize turtle"""
    turtle.up()
    turtle.title("Shapes")
    turtle.pensize(4)

def main():
    """Draw one set of embedded shapes"""
    init()

    def draw_square():
        turtle.color('green')
        turtle.down()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.up()

    def draw_circle():
        turtle.color('red')
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.down()
        turtle.circle(25)
        turtle.up()
        turtle.left(90)
        turtle.back(25)
        turtle.right(90)
        turtle.back(50)

    def draw_triangle():
        turtle.color('blue')
        turtle.down()
        turtle.forward(25)
        turtle.left(120)
        turtle.forward(25)
        turtle.left(120)
        turtle.forward(25)
        turtle.left(120)
        turtle.down()

    def draw_shapes():
        draw_square()
        draw_circle()
        draw_triangle()

    draw_shapes()
    turtle.color('black')
    turtle.right(180)
    draw_shapes()
    turtle.done()

main()