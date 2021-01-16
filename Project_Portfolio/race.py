import time
import turtle
from turtle import Turtle
from random import randint
#open window on screen
window=turtle.Screen()
window.title("Happy New Year :)") 
turtle.bgcolor("darkred")
turtle.color("White")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("Happy New Year!", font=("Verdana",30))
turtle.penup() 

#2020 line

turtle.setpos(-400, -180)
turtle.color("wheat")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#2021 reaching line

stamp_size=20
square_size=15
reaching_line=200

turtle.color("wheat")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

#drawing the reaching line

for i in range(10):
    turtle.setpos(reaching_line, (150-(i * square_size*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(reaching_line, ((150 - square_size) - (j * square_size *2)))
    turtle.stamp()

turtle.hideturtle()

#Drawing the turtles

# turt 1
turtle1=Turtle()
turtle1.speed(0)
turtle1.color("cyan")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

# turt 2
turtle2=Turtle()
turtle2.speed(0)
turtle2.color("white")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# turt 3
turtle3=Turtle()
turtle3.speed(0)
turtle3.color("wheat")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# turt 4
turtle4=Turtle() 
turtle4.speed(0)
turtle4.color("chocolate")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -53)
turtle4.pendown()

# to pause the turtles before start of race for 1 second 
time.sleep(1)

#moving the turts

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

turtle.exitonclick()

















