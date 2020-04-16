import turtle
t = turtle

colors = ['blue', 'green', 'yellow', 'orange', 'red']

def pause():
    _ = raw_input("Press Enter to exit:")

def spiral(t, step, step_incr, angle):
    color_ind = 0
    colors_len = len(colors)
    t.pencolor(colors[color_ind])
    while True:
        t.forward(step)
        step = step + step_incr
        if step > 500:
            break
        t.right(angle)
        color_ind = (color_ind + 1) % colors_len
        t.pencolor(colors[color_ind])

    t.hideturtle()
    pause()

t.speed(-100)
spiral(t, 20, 5, 90.2)