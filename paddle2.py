from turtle import *
WIDTH=20
HEIGHT=100
X=350
Y=0

class Paddle:
    def __init__(self):
      X=350
      
      

    def create_ri(self):
       
      self.tr=Turtle('square')
      self.tr.setheading(90)
      self.tr.shapesize(stretch_len=5,stretch_wid=1)
      self.tr.penup()
      self.tr.color('white')
      self.tr.speed('fastest')
      self.tr.goto(x=350,y=0)
    def create_le(self):
      self.tl=Turtle('square')
      self.tl.setheading(90)
      self.tl.shapesize(stretch_len=5,stretch_wid=1)
      self.tl.penup()
      self.tl.color('white')
      self.tl.goto(x=-350,y=0)
      
 
    
    def UP(self):
      self.tr.forward(10)
      # self.tl.forward(20)

    def DOWN(self):
      self.tr.backward(10)
      # self.tl.backward(20)



