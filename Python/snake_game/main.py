from turtle import Screen, Turtle
from snake import Snake
import time
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    


        
        
        
        




Screen.exitonclick()
