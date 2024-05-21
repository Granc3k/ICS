from karel.stanfordkarel import *

"""
File: hospital_karel.py
------------------------------
Your job is to help Karel build new hospitals in
the places marked by each beeper in the original world.
"""


def main():
    while front_is_clear():
        move_between()
        build_hospital()

def move_between():
    while no_beepers_present():
        move()

def build_hospital():
    turn_left()
    build_wall()
    turn_right()
    move()
    turn_right()
    build_wall()
    turn_left()
    if front_is_clear():
        move()

def build_wall():
   if beepers_present():
       for i in range(2):
           move()
           put_beeper()
   else:
       put_beeper()
       for i in range(2):
           move()
           put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
