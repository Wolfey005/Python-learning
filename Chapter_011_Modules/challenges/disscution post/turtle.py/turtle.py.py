
#from turtle import*
from turtle import showturtle, forward, left, color, right
showturtle()
forward(100)
left(120)

#draw triangle
forward(100)
left(120)
forward(100)
#geometric patterns
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)