import turtle

bgc = turtle.Screen()
bgc.bgcolor("yellow")

ttle = turtle.Turtle()

ttle.color("black")
ttle.pensize(3)

## Draw a square
ttle.forward(100)
ttle.left(90)
ttle.forward(100)
ttle.left(90)
ttle.forward(100)
ttle.left(90)
ttle.forward(100)
ttle.left(90)

bgc.exitonclick()