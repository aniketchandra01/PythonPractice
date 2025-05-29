import random

import colorgram
from turtle import *
a = colorgram.extract('SpotPainting.jpg',6)
rgbColours = [(239, 0, 235), (236, 0, 240), (126, 0, 236), (199, 154, 115), (241, 26, 238), (225, 29, 122)]
#
# for colour in a:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb = (r,g,b)
#     rgbColours.append(rgb)
# print(rgbColours)   
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)  # RGB mode
screen.title("10x10 Dot Grid")
sam = Turtle()
sam.hideturtle()
sam.speed(0)
sam.penup()
dot_size = 20
spacing = 50
start_x = -spacing * 5
start_y = spacing * 5
sam.goto(start_x, start_y)
for row in range(10):
    for col in range(10):
        sam.dot(dot_size, random.choice(rgbColours))
        sam.forward(spacing)
        # Move to the start of next row
    sam.goto(start_x, start_y - (row + 1) * spacing)
screen.exitonclick()