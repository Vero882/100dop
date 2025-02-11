from turtle import Screen 
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake")
screen.tracer(0)

# Pause challenge 1 - Lesson 147 3:28 - Create 3 turtles and position them in a line with no gaps. Each turtle should be a square.
# Pause chellenge 2 - Lesson 149 1:51 - Create a snake class, and move all code relating to the snake into that class. 
# Pause challenge 3 - Lesson 150 2:43 - Create methods in the snake class that changes the snake direction.
# Pause challenge 4 - Lesson 150 9:16 - Prevent the snake from reversing direction in the snake class.

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()