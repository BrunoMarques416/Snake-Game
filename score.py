from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier",20,"normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.actual_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
              
    def update_score(self):
        self.write(f"Score: {self.actual_score}", align =ALIGNEMENT, font=FONT)
               
    def increase_actual_score(self):
        self.actual_score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ", align =ALIGNEMENT, font=FONT)
    