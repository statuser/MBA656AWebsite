import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

def make_square(a_turtle):
    for i in range(0, 4):
        a_turtle.forward(100)
        a_turtle.right(90)

make_square(slowpoke)

speedy = turtle.Turtle()
speedy.shape('turtle')
speedy.color('blue')
speedy.right(45)

make_square(speedy)

turtle.mainloop()