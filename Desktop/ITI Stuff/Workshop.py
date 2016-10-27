import turtle

wn=turtle.Screen()

alex=turtle.Turtle()
alex.speed(10)
n=360

for sideNum in ["red", "green", "blue", "yellow", "black"]:
    alex.color("sideNum")
    alex.forward(75)
    alex.left(360/n)

wn.exitonclick()
