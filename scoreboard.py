import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.level}", font=FONT, align="left")

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align="center")

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
