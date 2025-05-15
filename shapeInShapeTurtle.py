from turtle import *
import random

sam = Turtle()
screen = Screen()
screen.screensize(1920,1080)
screen.bgcolor("black")
sam.speed(1)
screen.delay(7)
sides = 3
colours = ("white","green","red","blue","pink","orange")
while sides != 12:
    sam.color(random.choice(colours))
    for x in range(0,sides):
        sam.forward(100)
        sam.left((180-(((sides - 2) * 180)/sides)))
    sides += 1



screen.exitonclick()