import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. states game")
screen.addshape(image)
screen.bgpic(image)


df = pandas.read_csv("50_states.csv")
state = df.state
list_state = state.to_list()
print(list_state)

trial = 0
while trial < 50:
    answer_state = screen.textinput(title=f"{trial}/50 States Correct", prompt="What's another state' name?")
    good_answer = answer_state.title()

    # print(good_answer)
    # print(df[state == good_answer])

    if good_answer in list_state:
        # print(df[state == good_answer])
        full = (df[state == good_answer])
        x = int(full.x)
        y = int(full.y)
        position = x, y
        # print(position)
        trial += 1
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(position)
        turtle.write(arg=good_answer)

        list_state.remove(good_answer)

    if good_answer == "Exit":
        break

print(list_state)
new_file = pandas.DataFrame(list_state)
new_file.to_csv("states_to_learn.csv")




