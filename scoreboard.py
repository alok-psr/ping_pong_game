from turtle import *

class Scoreboard:
    def __init__(self) :
        self.score=0
        self.xpos=0
        self.ypos=300
    def create(self):
        self.t=Turtle()
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(self.xpos,self.ypos)
    def show_score(self):
        self.score+=1
        self.t.pendown()
        self.t.write(self.score)
        self.t.penup()
        self.t.clear()