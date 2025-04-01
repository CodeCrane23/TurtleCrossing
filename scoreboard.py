from turtle import Turtle

FONT=("Courier", 18, "bold")
FONT2=("Courier", 18, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-238,260)
        self.hideturtle()
        self.level=1
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", False, "center", FONT)
    def refresh_score(self):
        self.level+=1
        self.clear()
        self.write_score()
    def game_over(self):
        self.goto(0,0)
        self.write(">>>GAME OVER<<<", False, "center", FONT2)