import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

content = pd.read_csv("50_states.csv")
all_states = content["state"].to_list()

guessed_states = []

count = 0
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="whats another state name").title()
    print(answer_state)

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        # for states in all_states:
        #     if states not in guessed_states:
        #         missed_states.append(states)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states to learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = content[content.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





screen.exitonclick()