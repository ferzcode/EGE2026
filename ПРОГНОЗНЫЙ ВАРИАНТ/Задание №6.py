from turtle import *
tracer(0)

screensize(5000, 5000)
k = 20

right(45)
for i in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
right(90)
forward(20 * k)
right(90)
for i in range(2):
    forward(10 * k)
    right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()