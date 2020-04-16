import turtle

t = turtle.Turtle()
t.speed(0)
t.color("yellow", "red")
t.width(3)

for petal in range(36):
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()
    t.right(10)
