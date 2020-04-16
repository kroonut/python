import turtle
import random

# change the color of the background
screen = turtle.Screen()
screen.bgcolor("#FFFFE0")

# the number of turtles to create and what color to create them with
colors = ["black", "red", "orange", "green"]

# size of our box
box_size = 500

# create a new turtle with a certain color
def create_turtle(color):
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)
        t.shape("turtle")
        t.color(color)
        return t

# create a list of turtles from a list of colors
def create_turtles(colors):
        turtles = []
        for color in colors:
                t = create_turtle(color)
                turtles.append(t)
        return turtles


# stamp and move the turtle
def move_turtle(t):
        t.stamp()
        angle = random.randint(-90, 90)
        t.right(angle)
        distance = random.randint(50, 100)
        t.forward(distance)

# is the turtle outside the box?
def is_turtle_outside_box(t, size):
        outside_box = False
        x = t.xcor()
        y = t.ycor()
        if x < (size / -2)  or x > (size / 2):
                outside_box = True
        if y < (size / -2) or y > (size / 2):
                outside_box = True
        return outside_box

# create our list of turtles
turtles = create_turtles(colors)

# use the first turtle to draw our boundary box
t1 = turtles[0]
t1.penup()
t1.goto(box_size / 2, box_size / 2)
t1.pendown()

for side in range(4):
        t1.right(90)
        t1.forward(box_size)

t1.penup()
t1.goto(0, 0)
t1.pendown()

# move all the turtles a hundred times
for move in range(100):

        # move a particular turtle from our list of turtles
        for a_turtle in turtles:
                move_turtle(a_turtle)

                # is the turtle outside the boundary box?
                if is_turtle_outside_box(a_turtle, box_size) == True:

                        # turn the turtle around and move it back
                        a_turtle.right(180)
                        a_turtle.forward(100)