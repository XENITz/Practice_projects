from turtle import  Turtle, Screen

tim = Turtle()
Screen = Screen()

def move_forwards():
    tim.forward(30)
def move_backwards():
    tim.backward(30)
    
def turn_left():    
    tim.left(25)
    #commmen\
        
def turn_right():
    tim.right(25)
    dasd
    hi = "Fsdfsd"
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

Screen.listen()
Screen.onkey(key="w", fun=move_forwards)
Screen.onkey(key="s", fun=move_backwards)
Screen.onkey(key="a", fun=turn_left)
Screen.onkey(key="d", fun=turn_right)
Screen.onkey(key="c", fun=clear)

Screen.exitonclick()
