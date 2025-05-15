import turtle
from turtle import *
import random

sam = Turtle()
screen = Screen()
screen.screensize(1920,1080)
turtle.colormode(255)
screen.title("Spirograph")
sam.speed(7)
sam.hideturtle()
screen.delay(0)
x = 0
y = 0
while 1:
    sam.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    sam.circle(100)
    sam.circle(0,5)









