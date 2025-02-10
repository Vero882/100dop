from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():  
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# Listener example:
# screen.listen()
# # When usuing a method you haven't created yourself, use keyword arguments instead of positional arguments
# # This is an example of a higher order function (onkey) that takes in a function (move_forwards) as an argument
# screen.onkey(fun=move_forwards, key="space") # When a function is passed as an argument, don't use parentheses ex move_forwards()

# TODO: Keybinds: W = Forward, S = Backwards, A = Counter-clockwise, D = Clockwise, C = Clear
# Pause challenge 1 - Lesson 141 1:07 - Build an etch-a-sketch program utilizing the keybinds listed above

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()