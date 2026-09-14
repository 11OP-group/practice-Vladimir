from turtle import *

shape("turtle")
screensize(1000,10000)
k=10

left(90)
pendown()

for i in range(4):
    forward(5*k)
    right(90)
penup()
right(90)
forward(10*k)
pendown()
for i in range(4):
    forward(5*k)
    left(90)
penup()
forward(5*k)
right(90)
forward(5*k)
pendown()
forward(5*k)
right(90)
forward(15*k)
right(90)
forward(5*k)
done()




