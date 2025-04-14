from turtle import Turtle, Screen
import random

# Set up turtle
t = Turtle()
t.speed("fastest")  
t.pensize(2)
t.hideturtle()

# Create a screen
screen = Screen()
screen.bgcolor("black")  

# Function to return a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Set turtle to use RGB mode
screen.colormode(1.0)

# Draw the spirograph
def draw_spirograph(gap_angle):
    for _ in range(int(360 / gap_angle)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap_angle)

draw_spirograph(5)  

screen.exitonclick()
