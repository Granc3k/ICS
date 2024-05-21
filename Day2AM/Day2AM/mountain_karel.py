from karel.stanfordkarel import *

"""
File: mountain_karel.py
------------------------------
At present, this file does nothing. Your job is to place
a beeper at the top of the mountain. You should make sure
that your program works for all of the sample mountain worlds
supplied in the starter folder.
"""


def main():
    while front_is_blocked():
        climb_up()
    while front_is_clear():
        put_beeper()
        while front_is_clear():
            climb_down()

def climb_up():
    turn_left()
    move()
    turn_right()
    move()

def climb_down():
        move()
        turn_right()
        move()
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
