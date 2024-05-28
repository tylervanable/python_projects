"""
    Draw rectangles stacked on top of each other, like blocks.
    
    Tyler
    2/3/24
"""


import turtle

# Set the pen's position and draw a 400x400 px square.
turtle.penup()
turtle.setpos(-200,-200)
turtle.pendown()
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)

# Divy the square into four horizontal rectangles
turtle.left(180)
turtle.forward(100)
turtle.right(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(400)




