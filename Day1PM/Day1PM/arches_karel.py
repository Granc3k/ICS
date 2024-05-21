from karel.stanfordkarel import *

"""
File: arches_karel.py
------------------------------
When you finish writing code in this file, arches_karel should
solve the "repair the quad" problem (or Charles Bridge, or Efes).
"""


def main():
    for i in range(3):
        build_column()
        move_four()
    build_column()

def build_column():
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_around()
    move_four()
    turn_left()

def move_four():
    for i in range(4):
        move()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
