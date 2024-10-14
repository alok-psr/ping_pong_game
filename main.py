from turtle import *
from paddle2 import Paddle
from bound import Bound
s=Screen()
s.tracer(0)
s.setup(height=620,width=820)
s.title('PONG GAME(BY ALOK)')
s.bgcolor('black')
s.listen()

pad_ri=Paddle()
pad_ri.create_ri()

pad_le=Paddle()
pad_le.create_le()

boundry=Bound()
boundry.boundry()
boundry.net()


s.onkeypress(key='s',fun=pad_ri.DOWN)
s.onkeypress(key='w',fun=pad_ri.UP)



game_on=True
while game_on:
    s.update()


    












s.exitonclick()
