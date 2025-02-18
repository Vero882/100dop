from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day24/snake/data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_highscore(self):
        with open("day24/snake/data.txt", mode="w") as data:
            data.write(str(self.score))

    def reset(self):
        if self.score > self.highscore:
            self.update_highscore()
        self.score = 0
        with open("day24/snake/data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
