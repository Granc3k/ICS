from karel.stanfordkarel import *

"""
File: stripe_karel.py
------------------------------
At present, this file does nothing. Your job is to place
a line of beepers on every odd row. You can assume that there
are an odd number of rows in the world, and you should make sure
that your program works for all of the sample stripe worlds.
"""


def main():
    for i in range(3):
        build_stripe()
        if no_beepers_present():
            put_beeper()
        turn()

def build_stripe():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()

def turn():
    if facing_east():
        turn_left()
        if front_is_clear():
            move_two()
            turn_left()
        else:
            turn_left()
    else:
        turn_right()
        move_two()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def move_two():
    for i in range(2):
        move()

if __name__ == "__main__":
    run_karel_program()
