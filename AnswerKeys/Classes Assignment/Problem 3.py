import turtle


def draw_shape(this_turtle, sides):
    for _ in range(sides):
        this_turtle.forward(100)
        this_turtle.right(360 / sides)


my_turtle = turtle.Turtle()

draw_shape(my_turtle, 3)
draw_shape(my_turtle, 4)
draw_shape(my_turtle, 6)
draw_shape(my_turtle, 20)

turtle.done()
