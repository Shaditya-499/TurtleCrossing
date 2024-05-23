COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARYPLACEMENTS=[]
from turtle import Turtle
import random
for i in range(-270,280,20):
    CARYPLACEMENTS.append(i)


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.placecars()

    def placecars(self):
        choosenycors = random.sample(CARYPLACEMENTS, 5)
        j=0
        for i in choosenycors:
            car = Turtle()
            car.shape("square")
            car.color(COLORS[j])
            j+=1
            car.shapesize(1,2)
            car.penup()
            car.setheading(180)
            car.goto(300, i)
            (self.cars).append(car)

    def movecars(self):
        for i in self.cars:
            i.forward(STARTING_MOVE_DISTANCE)
            if i.xcor()<=-300:
                self.cars.remove(i)
                i.hideturtle()

