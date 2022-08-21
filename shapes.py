from turtle import *

bgcolor('black')
speed(0.2)
hideturtle()
for i in range(120):
    color('red')
    circle(i*0.5)
    color('blue')
    circle(i*0.4)
    color('pink')
    circle(i*0.3)
    right(3)
    forward(3)
done()