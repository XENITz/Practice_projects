from turtle import Screen, Turtle
from snake import Snake
import time
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)

snake = Snake()

Screen.listen()
Screen.onkey(key="a", fun=snake.left)
Screen.onkey(key="d", fun=snake.right)
Screen.onkey(key="s", fun=snake.down)
Screen.onkey(key="w", fun=snake.up)

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.05)
    
    snake.move()

    


        
        
        
        




Screen.exitonclick()
