from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -60, -30, 0, 30, 60]
all_turtles = []


for turtles_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtles_index])
    all_turtles.append(new_turtle)
    
while True:
    for turtle in all_turtles:
        steps = random.randint(0, 10)
        turtle.forward(steps)
        if turtle.xcor() >= 100:
            turtle.stamp()
            break






screen.exitonclick()