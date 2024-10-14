from turtle import*

class Bound:
    def __init__(self):
        self.li=[]
        self.t=Turtle('square')
    def boundry(self):
        
        self.t.color('grey')
        self.t.penup()
        self.t.pensize(10)
        self.t.goto(x=400,y=300)
        self.t.pendown()
        self.t.goto(-400,300)
        self.t.color('red')
        self.t.goto(-400,-300)
        self.t.color('grey')
        self.t.goto(400,-300)
        self.t.color('red')
        self.t.goto(400,300)
        self.t.penup()
    def net(self):
        self.t.color('yellow')
        self.t.pensize(2)
        self.t.goto(0,310)
        self.t.pendown()
        self.t.setheading(270)

        for i in range(16):
            self.t.forward(20)
            self.t.penup()
            self.t.forward(20)
            self.t.pendown()
        self.t.hideturtle()

