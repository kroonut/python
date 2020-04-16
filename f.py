from turtle import *

for circle in range(0, 360, 10):
    setheading(circle)
    forward(100)
    write(str(circle) + '°')
    backward(100)

    