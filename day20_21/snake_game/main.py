from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

## Pause challenge 1 - Lesson 154 2:09 - Make food class inherit from turtle class.
## Pause challenge 2 - Lesson 155 2:18 - Create a scoreboard class that inherits from turtle.
## Pause challenge 3 - Lessong158 6:02 - Refactor the tail collision to use slicing instead of the pass if statement.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()