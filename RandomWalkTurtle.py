import turtle
from turtle import *
import random

sam = Turtle()
screen = Screen()
screen.screensize(1920,1080)
turtle.colormode(255)
screen.title("Random Walk")
sam.speed(1)
sam.pensize(13)
sam.hideturtle()
screen.delay(7)
direction = [sam.right,sam.left]
angle = [0,90,180,270]
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta","black","pink","gray"]
while 1:
    sam.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    random.choice(direction)(random.choice(angle))
    sam.forward(25)










