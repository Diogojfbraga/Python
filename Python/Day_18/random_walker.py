from turtle import Turtle, Screen
import random

t = Turtle()
t.shape("turtle")
t.speed("fastest")  # Make it zoom!
t.pensize(15)         # Make the path more visible

colors = ["red", "blue", "green", "gray", "purple", "orange", "yellow", "cyan"]

# Infinite-ish random movement
for _ in range(200):  # You can increase this number for longer movement
    t.color(random.choice(colors))
    t.setheading(random.choice([0, 90, 180, 270]))  # Pick a random compass direction
    t.forward(random.randint(10, 30))  # Move a random distance


screen = Screen()
screen.exitonclick()