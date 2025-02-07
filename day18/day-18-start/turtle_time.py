from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan") # Color is referenced from the tkinter color names

# Pause challenge 1 - Lesson 129 0:33 - Draw a 100x100 square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Pause challenge 2 - Lesson 131 1:00 - Draw a dashed line
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Pause challenge 3 - Lesson 132 0:27 - Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon each a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# for i in range(3, 11):
#     timmy.pencolor(random_color())
#     for j in range(i):
        
#         timmy.forward(100)
#         timmy.right(360/i)

# Pause challenge 4 - Lesson 133 1:47 - Draw a random walk with random colors, thicker lines, and faster
# timmy.speed(10)
# timmy.pensize(10)

# for i in range(200):
#     timmy.pencolor(random_color())
#     timmy.forward(25)
#     timmy.setheading(random.choice([0, 90, 180, 270]))

# Pause challenge 5 - Lesson 134 1:10 - Draw a spirograph with random colors
timmy.pensize(2)
for i in range(36):
    timmy.pencolor(random_color())
    timmy.speed(0)
    timmy.circle(100)
    timmy.left(10)



    

screen = Screen()
screen.exitonclick()

