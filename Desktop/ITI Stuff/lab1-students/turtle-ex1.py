import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line
t.pendown()
t.pencolor("red")
t.goto(0, -150)
t.goto(0, 150)
t.goto(0,0)
t.pencolor("Blue")
t.goto(150,0)
t.goto(-150,0)
t.pencolor("Green")
t.goto(0,0)
t.goto(100,100)
t.goto(-100,-100)
t.penup()
t.goto(-100,100)
t.pendown()
t.goto(100, -100)
t.goto(0,0)
#Circle drawing starts
t.goto(0,-7.5)
t.circle(7.5)
t.penup()
t.goto(0, -25)
t.pendown()
t.circle(30)
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(55)
t.goto(0,-75)
t.circle(80)



