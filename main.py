import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
move_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(move_speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detecting collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting the turtle reaching the other end
    if player.ycor() > 290:
        player.reset_position()
        move_speed *= 0.5
        scoreboard.increase_level()

screen.exitonclick()
