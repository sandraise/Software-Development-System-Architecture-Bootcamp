import turtle

bgc = turtle.Screen()
bgc.bgcolor("pink")

ttle = turtle.Turtle()

ttle.color("grey")
ttle.pensize(3)

## Draw a rectangle
ttle.forward(150)
ttle.left(90)
ttle.forward(60)
ttle.left(90)
ttle.forward(150)
ttle.left(90)
ttle.forward(60)
ttle.left(90)

bgc.exitonclick()