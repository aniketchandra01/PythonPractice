from turtle import *
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Race")

colors = ["red", "pink", "orange", "yellow", "blue"]
random.shuffle(colors)
turtles = []

start_x = -350
start_y = 125
spacing = 60

# Create turtles and position them
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(start_x, start_y - spacing * i)
    turtles.append(t)

finish_line = 350
race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(10, 20))
        if t.xcor() >= finish_line:
            race_on = False
            winner = t.color()[0]
            print(f"The winner is the {winner} turtle!")
            break


screen.mainloop()

