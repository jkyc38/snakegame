from turtle import Turtle
ALIGN = 'center'
FONT = ("Times New Roman",15, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setpos(x=0,y=280)
        self.update_sb()

    def update_sb(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGN, font=FONT)

    def update(self):
        self.score+=1
        self.clear()
        self.update_sb()
    
    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", move=False, align=ALIGN, font=24)

        

