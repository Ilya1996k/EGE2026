from turtle import*
k=20
screensize(1000,1000)
tracer(20)
left(90)
down()
for d in range(2):
    forward(k*1)
    left(270)
    forward(16*k)
    right(90)
up()
back(4*k)
right(90)
forward(10*k)
left(90)
down()
for d in range(2):
    forward(k*17)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(k*x,k*y)
        dot(5,"green")
done()
