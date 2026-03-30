from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(4):
    penup()
    forward(50 * k)
    left(135)
    pendown()

for i in range(2):
    forward(102 * k)
    left(120)
    forward(182 * k)
    left(60)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()