import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.move()

    # Create cars randomly
    if random.randint(1, 6) == 1:
        carmanager.create_car()

    # Detect collision with car
    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()



screen.exitonclick()