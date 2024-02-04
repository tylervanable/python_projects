"""
    Draw the tic-tac-toe hash sign centered around the origin.
    Tyler
    ~1/28/24
"""


import turtle

# Two horizontal lines
turtle.penup()
turtle.setpos(-50,25)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.setpos(-50,-25)
turtle.pendown()
turtle.forward(100)

# Two vertical lines
turtle.penup()
turtle.setpos(-25,-50)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.setpos(25,-50)
turtle.pendown()
turtle.forward(100)
turtle.pendown()


