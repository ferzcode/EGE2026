from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(2):
    forward(20 * k)
    left(270)
    forward(12 * k)
    right(90)

penup()
forward(9 * k)
right(90)
forward(7 * k)
left(90)
pendown()
for i in range(2):
    forward(13 * k)
    right(90)
    forward(6 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()