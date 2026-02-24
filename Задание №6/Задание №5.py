from turtle import *

screensize(7000, 7000)
tracer(0)

k = 40
for i in range(10):
    forward(7 * k)
    right(120)

penup()
for x in range(-50, 50):
    for y in range(-50 , 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()