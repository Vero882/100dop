from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bets", prompt="Which turtle will win the race? Enter a color: ")

# List of colors for turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

starting_y = -100

# Pause challenge 2 - Lesson 143 10:36 - Create six turtles with different colors that all start on the left side of the screen.
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=starting_y)
    starting_y += 45
    all_turtles.append(turtle)
    
if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            race_on = False
            

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(-230, 100)


screen.exitonclick()