import turtle
turtle.tracer(10)


for i in range(180):
    turtle.forward(100)
    turtle.right(30)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(50)
    turtle.right(30)

    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()

    turtle.right(2)

turtle.done()
