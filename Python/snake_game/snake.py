from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.head = self.snakes_list[0]
        
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
        self.head.forward(MOVE_DISTANCE)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self): 
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)


        