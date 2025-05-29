from turtle import *

sam = Turtle()
screen = Screen()

def move_forward():
    sam.forward(10)
def move_backwards():
    sam.backward(10)
def turn_right():
    sam.right(10)
def turn_left():
    sam.left(10)
def clear():
    sam.goto(0,0)
    sam.clear()

screen.bgcolor("black")
sam.color("white")
sam.speed(0)
screen.screensize(1280,720)
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")


screen.exitonclick()