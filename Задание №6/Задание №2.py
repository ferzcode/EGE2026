from turtle import *

screensize(7000, 7000)
tracer(0)

k = 20

for i in range(5):
    forward(30 * k)
    right(90)
    forward(40 * k)
    right(90)
penup()
forward(20 * k)
right(90)
forward(5 * k)
right(90)
pendown()
for x in range(7):
    forward(10 * k)
    right(90)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()