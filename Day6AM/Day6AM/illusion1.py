"""
File: illusion1.py
------------------------
This program draws an optical illusion of a checkerboard pattern.
"""

from graphics import Canvas


# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.
CANVAS_WIDTH = 540
CANVAS_HEIGHT = 430

# The size of each dimension of the square. use this!
SIZE = 100

# The space between two squares. Use this!
GAP = 10

LINES = 4
SQUARES = 5
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 1")
    y1 = 0
    for j in range(LINES):
        x1 = 0
        for i in range(SQUARES):
            y2 = y1 + SIZE
            square = canvas.create_rectangle(x1, y1, x1 + SIZE, y2)
            x1 += SIZE + GAP
            canvas.set_color(square, "black")
        y1 += SIZE + GAP
    canvas.mainloop()


if __name__ == '__main__':
    main()
