from karel.stanfordkarel import *

"""
File: collect_newspaper_karel.py
------------------------------
At present, the collect_newspaper_karel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    move_two()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move_two()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
def move_two():
    for i in range (2):
        move()
if __name__ == "__main__":
    run_karel_program()
