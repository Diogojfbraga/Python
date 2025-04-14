from turtle import Turtle, Screen
import random

import turtle as t

t = Turtle()

sides = 4

# angle = 360 / x
from random import randrange

color_things = (["red", "blue", "green", "gray", "purple", "orange"])


print(color_things)



t.shape("turtle")

for _ in range(5):

    for _ in range(sides):

        t.forward(100)
        t.right(360/sides)
        
        
    
    t.end_fill() 
    sides += 1
    # t.pendown()
    # t.forward(5)
    # t.penup()
    # t.forward(5)


 
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)




screen = Screen()
screen.exitonclick()