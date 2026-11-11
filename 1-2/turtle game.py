# a121_catch_a_turtle.py
# import statements

import turtle as trtl
painter = trtl.Turtle()

# game configuration

spot_color = "red"
spot_shape = "circle"
spot_shape_size = 1


# initialize turtle

def draw_spot():
    painter.fillcolor(spot_color)
    painter.begin_fill()
    painter.circle(30)
    painter.end_fill()

draw_spot()


# game functions


# events



wn = trtl.Screen()
wn.mainloop()