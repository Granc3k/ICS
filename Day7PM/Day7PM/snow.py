"""
File: snow.py
-------------
Animates snow falling from the top to the bottom of the screen.  Snowflakes will be randomly added at the top at
random locations, and animated downwards together until they reach the bottom of the screen.
"""

from graphics import Canvas
import random
import time

ANIMATION_DELAY_SECONDS = 0.01
SNOWFLAKE_DIAMETER = 10


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Snow")
    
    # TODO: your code here!

    canvas.mainloop()


if __name__ == '__main__':
    main()
