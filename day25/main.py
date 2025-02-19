import turtle
import pandas

data = pandas.read_csv("day25/50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
user_answers = []

while game_is_on:
    user_answer = screen.textinput(title=f"{len(user_answers)}/50 States Correct", prompt="What's another state's name?")
    user_answer.title()

    if (data.state == user_answer).any():
        if user_answer not in user_answers:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == user_answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(user_answer)
            user_answers.append(user_answer)
    
    if len(user_answers) == len(data.state):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        t.write("You've got all 50 states! You win!", align="center", font=("Arial", 24, "normal"))
        game_is_on = False
    



turtle.mainloop()
# screen.exitonclick()