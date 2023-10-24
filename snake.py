from turtle import Turtle
start_pos = [(0,0), (-20,0), (-40,0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in start_pos:
            self.add_segment(pos)
    def add_segment(self, pos):
        block = Turtle('turtle')
        block.color('white')
        block.penup()
        block.setpos(pos)
        self.segments.append(block)
    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for blocks in range(len(self.segments)-1,0,-1):
            x = self.segments[blocks-1].xcor()
            y = self.segments[blocks-1].ycor()
            self.segments[blocks].goto(x,y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
            self.move()
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
            self.move()
    
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
            self.move()
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
            self.move()
    def create_body(self):
        block = Turtle('square')
        block.hideturtle()
        block.color('white')
        block.penup()
        self.segments.append(block)
        block.goto(self.segments[len(self.segments)-1].pos())
        block.showturtle()
       


