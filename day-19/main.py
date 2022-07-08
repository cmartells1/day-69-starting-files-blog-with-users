from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "blue", "green", "purple", "yellow"]
y = -100


for turtle_index in range(0, 6):
    y += 30
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y)


screen.exitonclick()