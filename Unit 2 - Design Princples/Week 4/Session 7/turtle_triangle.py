import turtle

bgc = turtle.Screen()
bgc.bgcolor("green")

ttle = turtle.Turtle()

ttle.color("blue")
ttle.pensize(5)

## Draw a triangle
ttle.forward(50)
ttle.left(120)
ttle.forward(50)
ttle.left(120)
ttle.forward(50)
ttle.left(120)

bgc.exitonclick()