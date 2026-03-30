from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(3):
    forward(27 * k)
    right(90)
    forward(12 * k)
    right(90)

penup()
backward(4 * k)
right(90)
forward(6 * k)
left(90)
pendown()
for i in range(4):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()