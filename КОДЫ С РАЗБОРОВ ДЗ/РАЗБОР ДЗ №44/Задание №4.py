from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
right(30)
for i in range(18):
    forward(11 * k)
    right(120)
    forward(11 * k)
    right(60)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()