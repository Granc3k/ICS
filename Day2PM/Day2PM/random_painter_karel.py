from karel.stanfordkarel import *

"""
File: random_painter_karel.py
------------------------------
Your job is to paint random squares all over the world!
Pick two colors and choose randomly between them for each
square.
"""


def main():
    for i in range(8):
        move_stripe()
        turn()

def move_stripe():
    while front_is_clear():
        paint()
        if front_is_clear():
            move()
            paint()

def paint():
    if random(0.5):
        paint_corner(BLUE)
    else:
        paint_corner(RED)

def turn():
    if facing_east():
        turn_left()
        move()
        turn_left()
    else:
        turn_right()
        if front_is_blocked():
            turn_left()
        else:
            move()
            turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
