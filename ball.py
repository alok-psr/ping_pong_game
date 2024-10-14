from turtle import *

class Ball:
    def __init__(self):
        self.ball=Turtle('square')
    
    def move(self):
        def r_up (self):
            x,y=self.ball.pos()
            self.ball.goto(x+10,y+10)
        def r_down (self):
            x,y=self.ball.pos()
            self.ball.goto(x+10,y-10)
        def l_up (self):
            x,y=self.ball.pos()
            self.ball.goto(x-10,y+10)
        def l_down (self):
            x,y=self.ball.pos()
            self.ball.goto(x-10,y-10)
        