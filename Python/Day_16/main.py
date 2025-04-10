# from turtle import *

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral", "green")
# timmy.forward

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# timmy.forward(100)
# import sys
# print(sys.executable)

# timmy.color()


import sys
print(sys.executable)

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Poekmon Name", ["pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)
