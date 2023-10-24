from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.head.distance(food)<20:
        food.refresh()
        scoreboard.update()
        snake.extend()
    
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        game_on = False
        scoreboard.game_over()
    
    #detect collison with snake tail lol

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            scoreboard.game_over()
            game_on= False
        
        




screen.exitonclick()