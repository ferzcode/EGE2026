from turtle import *

screensize(5000, 5000)
tracer(0)

k = 40
right(315)
for i in range(7):
    forward(12 * k)
    right(45)
    forward(6 * k)
    right(135)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()