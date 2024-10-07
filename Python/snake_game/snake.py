from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snakes_list.append(snake)
    
    def move(self):
        for snake_num in range(len(self.snakes_list) - 1, 0, -1):
            x = self.snakes_list[snake_num - 1].xcor()
            y = self.snakes_list[snake_num - 1].ycor()
            self.snakes_list[snake_num].goto(x, y)

        self.snakes_list[0].forward(MOVE_DISTANCE)