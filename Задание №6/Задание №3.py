from turtle import *

screensize(7000, 7000)
tracer(0)

k = 25

for i in range(3):
    pendown()
    for i in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    penup()
    forward(5 * k)
    right(90)
    forward(5 * k)
    left(90)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()

