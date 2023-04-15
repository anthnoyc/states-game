import turtle
import pandas

text = turtle.Turtle()
text.hideturtle()
text.penup()
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guesses = []
score = 0
game_is_on = True
while score < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and not correct_guesses:
        state = data[data.state == answer_state]
        text.goto(int(state.x), int(state.y))
        text.write(f"{answer_state}", font=("Arial", 15, "normal"))
        score += 1
        screen.title(f"{score}/50 States Guessed")
        correct_guesses.append(answer_state)
    else:
        print("Game Over")
    if score == 50:
        print("You Completed the Map!")



