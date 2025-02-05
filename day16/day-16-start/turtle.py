# Practice creating an object from a class (blueprint) that someone has already created. 

# import turtle
from turtle import Turtle, Screen # This format simplifies the use of the code below.

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
# Pause Challenge 1 (Lesson 110: 12:53): Change the color of the turtle.
timmy.color("cyan4")

# Pause Challenge 2 (Lesson 110: 14:00): Get turtle to move forward 100 paces.
timmy.forward(300)

# Accessing attributes of the object is done with 'class.attribute'.

my_screen = Screen()
print(my_screen.canvheight) # Prints the height of the canvas in the terminal by accessing the 'cavheight' attribute.

# Access methods of the object by using 'class.method()'.
my_screen.exitonclick()

