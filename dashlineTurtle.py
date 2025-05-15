from turtle import *


sam = Turtle()
screen = Screen()
screen.title("Turtle")
screen.screensize(4000,3000)
screen.bgcolor("black")
sam.speed(1)
screen.delay(5)
sam.color("white")
for x in range(0,50):
    sam.forward(10)
    sam.penup()
    sam.forward(10)
    sam.pendown()


screen.exitonclick()

