"""
Joseph Vita
Lab 1

Python program writes out the phrase 'YOOT TOM' using the python 
turtle framework.
"""

import turtle
import math

 
""" 
	Main function creates the phrase 'YOOT TOM' by calling 
	the	correct functions in the correct order.
"""
def main():
    turtle.penup()
    letter_y()
    letter_o()
    letter_o()
    letter_t()
    space()
    letter_t()
    letter_o()
    letter_m()
    turtle.done()


"""
	space function draws a space between words that is 15 units long
"""
def space():
    turtle.penup()
    turtle.forward(15)


"""
	Creates the letter Y that is 20x20 pixels
"""
def letter_y():
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(-10*math.sin(30) + 1)
    turtle.backward(-10*math.sin(30) + 1)
    turtle.right(60)
    turtle.forward(-10*math.sin(30) + 1)
    turtle.penup()
    turtle.backward(-10*math.sin(30) + 1)
    turtle.right(150)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)


"""
	Creates the letter T that is 20x 20 pixels
"""
def letter_t():
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.backward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(5)


"""
	Creates the letter O (as a square shape) that is 20x 20 pixels
"""
def letter_o():
    turtle.pendown()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)


"""
	Creates the letter M that is 20x 20 pixels
"""
def letter_m():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(150)
    turtle.forward(math.sqrt(500))
    turtle.left(120)
    turtle.forward(math.sqrt(500))
    turtle.right(150)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(5)


"""
	tests space function
"""
def test_space():
    turtle.penup()
    turtle.forward(15)


"""
	Tests Y function
"""
def test_letter_y():
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(-10*math.sin(30) + 1)
    turtle.backward(-10*math.sin(30) + 1)
    turtle.right(60)
    turtle.forward(-10*math.sin(30) + 1)
    turtle.penup()
    turtle.backward(-10*math.sin(30) + 1)
    turtle.right(150)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(15)


"""
	Tests T function
"""
def test_letter_t():
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.backward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(5)


"""
	Tests O function
"""
def test_letter_o():
    turtle.pendown()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)


"""
	Tests M function
"""
def test_letter_m():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(150)
    turtle.forward(math.sqrt(500))
    turtle.left(120)
    turtle.forward(math.sqrt(500))
    turtle.right(150)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(5)
    

#test_letter_m()
#test_letter_o()
#test_letter_y()
#test_space()
#test_letter_t()

main() # calls main funtion to run program
