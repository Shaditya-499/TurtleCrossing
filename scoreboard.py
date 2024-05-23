FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.score=0
        self.scoreboardupdqate()

    def scoreboardupdqate(self):
        self.score+=1
        self.clear()
        self.write((f"level={self.score}"),False,"left",FONT)

    def gameover(self):
        self.clear()
        self.goto(-20,0)
        self.write((f"your score={self.score}"),False,"left",FONT)
        self.goto(-20,-20)
        self.write("game over", False, "left", FONT)

