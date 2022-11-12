import turtle
import pandas

# if you want to add additional countries/states or create a new data set (=Map) from scratch,
# set the map_name to name of the map you want to create/edit.
# Hint: it has to have a background image already saved with this exact name.
# Previously saved data is optional.

# the name of the map you want to edit (it has to have an image already saved with this exact name)
map_name = "africa"
# do you want to edit the current data for the map
append = True
# do not change this!!!! if it's not existing the dictionary with the available maps gets updated
existing = None

# creates a screen, loads the background and creates the turtle that will write the names on the screen
screen = turtle.Screen()
screen.bgpic(f"./maps/{map_name}.gif")
my_turtle = turtle.Turtle()
my_turtle.pu()
my_turtle.hideturtle()
my_turtle.color("red")


def get_existing_data():
    global existing
    try:
        # try to get existing data for the map.
        # if there is some, show the existing countries on the screen
        # and add their properties to the lists that will be converted to the data set that will be exported
        data = pandas.read_csv(f"./data/{map_name}.csv")
        for current in data.state:
            state = data[data.state == current]
            # i use .tolist()[0] since .item() returns an error,
            # if there are multible items with the same name in the list.
            # by using .tolist()[0] it just ignores every but the first item
            x = float(state.x.tolist()[0])
            y = float(state.y.tolist()[0])
            my_turtle.goto(x, y)
            my_turtle.write(arg=state.state.tolist()[0], align="center")
            countries.append(state.state.tolist()[0])
            xcors.append(x)
            ycors.append(y)

        # set existing to true, so that there won't be an additional entry in the map selector
        existing = True
    except FileNotFoundError:
        # if there is no data already saved,
        # set existing to true, so that there will be an additional map entry in the map selector,
        # so that the nwe map can be played
        existing = False


def get_mouse_click_coor(x, y):
    """
    get the coordinates of the mouse click, and ask for the name of the country the user clicked on.
    safe these properties to the lists that will be converted to the data set that will be exported
    after that, go to the according position and write the country name on the map
    """
    country = screen.textinput(title="", prompt="Which Country is this").title()
    print(country, x, y)
    countries.append(country)
    xcors.append(float(x))
    ycors.append(float(y))

    my_turtle.goto((x, y))
    my_turtle.write(arg=country, align="center")


def add_entry_to_map_selector():
    # open the map selector
    with open("./game_mode_data.py") as game_mode_data:
        game_mode_data_str = str(game_mode_data.read())
    # get all maps
    existing_game_mode_data = game_mode_data_str[0:-1]
    # format the new one
    new_game_mode_data = f',"{map_name}": {str("{")}"map": "./maps/{map_name}.gif",' \
                         f'"data": "./data/{map_name}.csv"{str("}")}'
    # add the new map
    complete_game_mode_data = existing_game_mode_data+new_game_mode_data+"}"
    print(complete_game_mode_data)

    # rewrite the map selector
    with open("./game_mode_data.py", mode="w") as game_mode_data:
        game_mode_data.write(complete_game_mode_data)


countries = []
xcors = []
ycors = []

get_existing_data()

# collect new data
turtle.onscreenclick(get_mouse_click_coor)
screen.mainloop()

# create the new data set, that can be exported as a csv file to play this map
new_data_lib = {
    "state": countries,
    "x": xcors,
    "y": ycors
}

# if this map is completely new, and the data set is going to get exported, add its entry to the map selector
if not existing and append:
    add_entry_to_map_selector()
# if checked, add the data set to the data sets
if append:
    pandas.DataFrame(new_data_lib).to_csv(f"./data/{map_name}.csv")
