import turtle as t
import random 


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = -100

for turtle_color in colors:
    racer = t.Turtle(shape = "turtle")
    racer.color(turtle_color)
    racer.penup()
    racer.goto(x = -375, y = y_cord)
    y_cord += 200/6

screen.exitonclick()