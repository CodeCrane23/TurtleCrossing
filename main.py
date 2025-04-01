from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

s=Screen()
s.colormode(255)
s.setup(width=600,height=600)
s.tracer(0)

player=Player()
score=ScoreBoard()
car_manager=CarManager()

s.listen()
s.onkey(player.up, "Up")

game_is_on=True
i=0.15
while game_is_on:

    time.sleep(i)
    s.update()

    car_manager.create_car()
    car_manager.move_cars()


    if player.ycor() > 279:
        score.refresh_score()
        player.reset_turtle()
        i*=0.8

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on=False




s.exitonclick()