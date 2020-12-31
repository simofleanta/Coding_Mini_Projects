import turtle

board=turtle.Screen()
t=turtle.Turtle()
t.color("red")
t.width()
t.speed(4)
t.shape('turtle')
t.shapesize(0.7)

for i in range(4):
    t.forward(300)
    t.left(90)

#inner lines in the square
t.penup()
t.goto(0,100)
t.pendown()
t.forward(300)
t.penup()
t.goto(0,200)
t.pendown()
t.forward(300)
t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(200,0)
t.pendown()
t.forward(300)


