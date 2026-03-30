from turtle import *

screensize(5000, 5000)
k = 20

tracer(0)
for i in range(5):
    forward(6 * k)
    right(90)
    forward( 3 * k)
    right(90)

penup()
forward(4 * k)
right(90)
forward(2 * k)
right(90)
pendown()

for i in range(8):
    forward(8 * k)
    right(90)
    forward(5 * k)
    right(90)

forward(4 * k)
right(90)
forward(2 * k)
left(90)
pendown()

for i in range(4):
    forward(5 * k)
    left(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

update()
done()