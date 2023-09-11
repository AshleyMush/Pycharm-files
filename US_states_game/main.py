import turtle
import pandas as pd

score = 0
total = 50


def add_point():
    global score
    score += 1
    # update_scoreboard()

# high_score = turtle.Turtle()
# high_score.penup()
# with open("score_data.txt", mode="r") as score_data_file:
#     highest_score = score_data_file.read()
# high_score.write(arg=highest_score )
# high_score.goto(300, 300)

screen = turtle.Screen()
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.title("U.S States Game")

# def get_mouse_click_coor(x,y):
#    print (x,y)
# # turtle.onscreenclick - WILL LISTEN TO THE ON SCREEN CLICK
# #Pass it in get_mouse_click_coor()
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()# equal to exit on click

# TODO 1 check if the guess is among the 50 states, get hold of all states
# All the states
data = pd.read_csv("50_states.csv")
# print(data)

states = data["state"]

guesses_list = []

# x_cor_List = x_cor.to_list()
# y_cor_List = y_cor.to_list()
#
# states_list = states.to_list()
# print(states_list)
# print(x_cor_List)
# print(y_cor_List)

# states_dict = {"states": state_list,
#                "x": x_cor_List,
#                "y": y_cor_List
#
#
#
#
# }

#
states_list = data["state"].to_list()
game_is_on = True

while score < 50 :

    answer_state = screen.textinput(title=f"{score}/ 50 States Correct", prompt="What's another state's name?").title()

    # guesses_list = [answer_state if answer_state in states_list and answer_state not in guesses_list]
    if answer_state in states_list and answer_state not in guesses_list:
        # This is to store the answers that are already in
        guesses_list.append(answer_state)

        print("Valid")
        # Create a turte that will print the name of state and go to the position
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[states == answer_state]
        # TODO ADD SCORE
        add_point()
        state_name = state_data.state.item()
        print(state_name)
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t.goto(x_cor, y_cor)
        t.write(arg=state_name)
    if answer_state == "Exit":
        with open("score_data.txt", mode="w") as score_data_file:
            score_data_file.write(f"{score}")

        states_to_learn_list = [missed_guess for missed_guess in states_list if missed_guess not in guesses_list]

        dict_file = {
            "state": states_to_learn_list

        }

        data_to_learn = pd.DataFrame(dict_file)
        data_to_learn.to_csv("states_to_learn.csv")
        screen.bye()

turtle.mainloop()

# answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
# if answer_state in states_list:
#     print("Valid")
#
# else:
#     print("Invalid")


# Compare co-ordinates using CSV
"""
if answer_state != state:
answer_state function()

"""
# Keep track of score
"""
if answer_state == state:
add_point()
update_scoreboard()

"""

# Randomly place the answer state
