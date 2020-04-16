#Program to draw concentric circles in Python Turtle
import turtle
  
t = turtle.Turtle()
for i in range(50):
  t.circle(10*i)
  t.up()
  t.sety((10*i)*(-1))
  t.down()