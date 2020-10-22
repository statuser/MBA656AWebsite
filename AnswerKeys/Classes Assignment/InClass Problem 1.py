import turtle

slowpoke = turtle.Turtle()

slowpoke.shape("turtle")


def make_star():
    for i in range(5):
        slowpoke.forward(100)
        slowpoke.right(144)


make_star()

turtle.done()
