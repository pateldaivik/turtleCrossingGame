import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player();
car_maneger = CarManager();
score = Scoreboard();

screen.listen()
screen.onkey(player.move_up,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_maneger.create_cars()
    car_maneger.move_cars()

    for car in car_maneger.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.ycor()>280:
        player.go_to_start()
        car_maneger.level_up()
        score.increase_level()


screen.exitonclick()
