from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "black", "green", "blue", "purple"]
y_positions = [-90, -60, -30, 90, 30, 60]
all_turtles = []
race_on = True


for turtles_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtles_index])
    all_turtles.append(new_turtle)
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 100:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} won the race")
            else:
                print(f"You lost! The {winner} won the race")
        steps = random.randint(0, 10)
        turtle.forward(steps)







screen.exitonclick()