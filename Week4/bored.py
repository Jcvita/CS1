from PIL import Image
import turtle
from turtle import Screen
import numpy as np


im = Image.open('C:\\Users\\Joe\\Documents\\CS1\\Week4\\monalisa.jpg')
turtle.tracer(0, 0)
turtle.screensize(len(list(np.asarray(im))[1]) + 100, len(list(np.asarray(im))) + 100)
turtle.penup()
turtle.setposition(-450, 388)
turtle.pendown()
turtle.right(90)


for y in range(len(list(np.asarray(im))[1])):
    turtle.penup()
    turtle.setposition(-450 + y, 388)
    turtle.pendown()
    for x in range(len(list(np.asarray(im)))):

        if (list(np.asarray(im))[x][y][0]) <= 255//1.75:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(1)

# print(len(list(np.asarray(im))[2]))
turtle.done()