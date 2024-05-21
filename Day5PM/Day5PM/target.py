"""
File: target.py
---------------
This program draws a red and white target symbol in the center of the screen.
"""

from graphics import Canvas

# The sizes of the concentric circles
BIG_CIRCLE_RADIUS = 150
MEDIUM_CIRCLE_RADIUS = 100
SMALL_CIRCLE_RADIUS = 50


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Target")

    # TODO: your code here - make sure to use functions!

    canvas.mainloop()


if __name__ == '__main__':
    main()
