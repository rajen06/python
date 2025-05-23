import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
    # create a turtle to write the state name on the map
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

   


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()


# screen.exitonclick()



# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)



# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])

# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# print(data_dict)

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")