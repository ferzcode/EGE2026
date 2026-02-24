from turtle import *

screensize(7000, 7000)
tracer(0)

k = 30

right(30)
pendown()
for x in range(10):
    forward(25 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()