from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(turtle_colors[turtle_index])
    tim.penup()
    tim.goto(x=-238, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
    
    while is_race_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")




# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")
screen.exitonclick()