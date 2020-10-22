import turtle

my_turtle = turtle.Turtle()

my_turtle.penup()
my_turtle.setposition((-120, 0))
my_turtle.pendown()
my_turtle.circle(100)
my_turtle.penup()
my_turtle.setposition((120, 0))
my_turtle.pendown()
my_turtle.circle(100)

turtle.done()