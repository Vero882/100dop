from turtle import Turtle

# STARTING_POSITIONS = [(-350, 0), (350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        
    def up(self):
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
            self.goto(self.xcor(), self.ycor() - 20)
