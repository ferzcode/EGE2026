from turtle import *

screensize(5000, 5000)
tracer(0)

k = 20

for i in range(3):
    forward(32 * k)
    right(90)
    forward(38 * k)
    right(90)

penup()
forward(25 * k)
right(90)
forward(21 * k)
left(90)
pendown()

for i in range(3):
    forward(29 * k)
    right(90)
    backward(18 * k)
    right(90)

penup()
for x in range(-70, 70):
    for y in range(-70, 70):
        goto(x * k, y * k)
        dot(3, "red")


update()
done()