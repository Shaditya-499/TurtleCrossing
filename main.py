import time
from turtle import Screen
from player import Player,FINISH_LINE_Y,STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
import gc

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#creating all the elements
player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(player.move,"Up")

screen.update()
game_is_on = True
counter=1
while game_is_on:
    time.sleep(player.REFRESH_RATE)
    if counter%15==0:
        carmanager.placecars()
    carmanager.movecars()
    if player.ycor() >= FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        player.REFRESH_RATE *= 0.9
        scoreboard.scoreboardupdqate()
    counter+=1
    screen.update()
    for car in carmanager.cars:
        if (car.distance(player)<20) :
            scoreboard.gameover()
            game_is_on=False
    gc.collect()
screen.exitonclick()