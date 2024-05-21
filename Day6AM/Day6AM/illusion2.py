"""
File: illusion2.py
------------------------
This program draws an optical illusion of an off-checkerboard pattern.
"""

from graphics import Canvas

# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

# The height of each row, and the size of each square. use this!
SQUARE_SIZE = 50

# The number of rows.  Use this!
NUM_ROWS = 10
SQUARES = CANVAS_WIDTH

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 2")
    for i in range(NUM_ROWS):
        for j in range(SQUARES):



    canvas.mainloop()


if __name__ == '__main__':
    main()
