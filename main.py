from turtle import Screen
import pandas
import scorekeeper
import writer
from game_mode_data import maps

# Asks the User which map hew wants to play and loads the required information
screen = Screen()
map_names = list(maps)
chosen_mode = ""
while chosen_mode not in map_names:
    chosen_mode = screen.textinput(title=f"Map selector",
                                   prompt=f"Which game mode would you like\n(You can choose between {map_names}):")

game_mode_data = maps[chosen_mode]
game_map = game_mode_data["map"]
data = game_mode_data["data"]

# Set everything up
screen.bgpic(game_map)

POSITION = screen.window_width() / 2 - 100, screen.window_height() / 2 - 70
STATES = pandas.read_csv(data)

found_states = []

writer = writer.Writer()
scorekeeper = scorekeeper.ScoreKeeper(POSITION, len(STATES))
scorekeeper.write_score()

# Game
while True:
    # Ask for User input, if none: End the game
    user_input = screen.textinput(title=f"Score: {scorekeeper.get_score()}",
                                  prompt="Please enter a state name:\n(Press Cancel to quit)")
    if user_input is None:
        break
    user_input = user_input.title()

    # Check if the guess of th user is right
    if not STATES[STATES.state == user_input].empty and user_input not in found_states:
        found_states.append(user_input)
        my_state = STATES[STATES.state == user_input]
        # write name on right spot on map and update the score
        writer.write_state(my_state)
        scorekeeper.add_score()
        scorekeeper.write_score()


# after the game ended:

def missed():
    """check for every country/state if the user found it, and if not, add it to a list of missed states.
    return this list as a dictionary with the missed_list under the key: state"""
    not_found = []
    for current_state in STATES.state:
        if current_state not in found_states:
            not_found.append(current_state)

    # create the dictionary, so that after converting it to a csv file, the column has a name (=state)
    not_found_dic = {
        "state": not_found
    }

    return not_found_dic


# create a list of all countries/states the user missed and safe it to a csv file
missed_dic = missed()
pandas.DataFrame(missed_dic).to_csv(f"./output/not_found_{chosen_mode}.csv")

screen.exitonclick()
