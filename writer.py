import turtle


class Writer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.speed(0)
        self.color("red")

    def write_state(self, my_state):
        """go to the coordinates of the state/country and write its name"""
        self.goto(x=float(my_state.x), y=float(my_state.y))
        self.write(arg=my_state.state.item(), align="center")
