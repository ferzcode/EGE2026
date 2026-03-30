from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(3):
    forward(2 * k)
    right(90)
    forward(3 * k)
    left(90)

right(180)
forward(6 * k)
right(90)
forward(9 * k)
penup()
backward(3 * k)
right(90)
pendown()
for i in range(2):
    forward(1  * k)
    right(90)
    forward(2 * k)
    left(90)

right(180)
forward(3 * k)
right(90)
forward(4 * k)
right(90)
forward(1 * k)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()