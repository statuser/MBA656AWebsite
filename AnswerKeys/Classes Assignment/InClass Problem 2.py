import turtle

slowpoke = turtle.Turtle()

slowpoke.shape('turtle')

slowpoke.color('blue')

slowpoke.circle(50)

speedy = turtle.Turtle()
speedy.shape('turtle')
speedy.color('red')
speedy.penup()
speedy.goto(0, 25)
speedy.pendown()
speedy.circle(10)

turtle.mainloop()


