"""
File: string_art.py
-------------------
This program creates string art using only straight lines.
"""

from graphics import Canvas

# Size of the canvas
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# The number of pixels between end points of each line
LINE_SPACING = 20

# The number of lines we will have to draw
NUM_LINES = CANVAS_WIDTH // LINE_SPACING


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("String Art")
    x1 = 0
    y1 = 0
    x2 = 0 + LINE_SPACING
    y2 = CANVAS_HEIGHT
    for i in range(NUM_LINES):
        canvas.create_line(x1, y1, x2, y2)
        y1 += LINE_SPACING
        x2 += LINE_SPACING


    canvas.mainloop()


if __name__ == "__main__":
    main()
