import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
correct_guesses = []


while len(correct_guesses) < 50 :
    answer_state = screen.textinput(title=f"{len(correct_guesses)} / 50 States Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        state = states_data[states_data.state == answer_state]
        # x = int(state.x)
        # y = int(state.y)
        t = turtle.Turtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.color("black")
        t.hideturtle()
        t.write(answer_state, align="center", font=("Courier", 8, "normal"))
        correct_guesses.append(answer_state)



