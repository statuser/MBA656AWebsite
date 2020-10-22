# Answers will vary
import turtle

my_turtle = turtle.Turtle()

# Draw Head
my_turtle.penup()
my_turtle.setposition((0, -100))
my_turtle.pendown()
my_turtle.circle(200)
# Draw Eyes
my_turtle.penup()
my_turtle.setposition((75, 75))
my_turtle.pendown()
my_turtle.circle(35)
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.setposition((-75, 75))
my_turtle.pendown()
my_turtle.circle(35)
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()

#Draw the mouth
my_turtle.penup()
my_turtle.setposition((-75, 0))
my_turtle.pendown()
my_turtle.right(45)
my_turtle.circle(110, 90)

# Turtle is the nose
my_turtle.penup()
my_turtle.setposition((0, 50))
my_turtle.left(45)

turtle.done()
