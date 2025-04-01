from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")

        self.penup()
        self.goto(0,-270)
        self.setheading(90)

    def up(self):
        self.fd(20)

    def reset_turtle(self):
        self.goto(0,-270)