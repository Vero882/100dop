import colorgram
from turtle import Turtle, Screen, colormode
import random

# This code section was provided by the class
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

colormode(255)

timmy = Turtle()
screen = Screen()
screen.setup(width=1100, height=1100)

timmy.shape("turtle")
timmy.color("cyan4")
timmy.pensize(10)
timmy.speed("fastest")
timmy.teleport(-450, -450)

def draw_row():
    for _ in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(100)
        timmy.pendown()

def move_to_next_row():
    timmy.penup()
    timmy.teleport(-450, timmy.ycor() + 100)
    timmy.pendown()

for i in range(10):
    draw_row()
    move_to_next_row()


screen.exitonclick()