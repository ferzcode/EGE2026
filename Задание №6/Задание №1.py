from turtle import *

screensize(7000, 7000)
tracer(0)

k = 25 # КОЭФФИЕНТ МАСШТАБА

for x in range(4):
    forward(9 * k)
    left(180)
    backward(10 * k)
    right(90)
penup()
backward(7 * k)
left(90)
forward(3 * k)
right(90)
pendown()
for x in range(2):
    forward(17 * k)
    left(90)
    forward(20 * k)
    left(90)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")


update()
done()