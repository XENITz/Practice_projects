from turtle import Screen, Turtle
import time
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snakes_list = []

##CREATE SNAKE
for position in starting_positions:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    snakes_list.append(snake)



game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.1)
    
    for snake_number in range(len(snakes_list) - 1, 0, -1):
        x = snakes_list[snake_number - 1].xcor()
        y = snakes_list[snake_number - 1].ycor()
        snake[snake_number].goto(x, y)
    snake[0].forward(20)

#
        
        
        
        




Screen.exitonclick()
