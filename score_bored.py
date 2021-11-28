from turtle import Turtle,Screen
ALIGNMENT="center"
FONT="Courier",24,"normal"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.color("white")
        self.write(f"score:{self.score}",ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.goto(0, 270)
        self.write(f"score:{self.score}", ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", ALIGNMENT, font=FONT)


