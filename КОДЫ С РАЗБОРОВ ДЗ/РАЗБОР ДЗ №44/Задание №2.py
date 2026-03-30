from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(2):
    forward(3 * k)
    right(90)
    forward(20 * k)
    right(90)

penup()
backward(8 * k)
right(90)
forward(9 * k)
left(90)
pendown()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()