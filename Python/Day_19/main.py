from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
