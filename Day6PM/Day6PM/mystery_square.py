"""
File: mystery_square.py
-------------------
This program creates a centered square that changes color randomly every second.
"""

from graphics import Canvas

# Needed for pausing for animation.  Don't remove this.
import time

# Size of the centered square
SQUARE_SIZE = 400

# Delay between color changes, in seconds
DELAY = 1


def main():
    canvas = Canvas(800, 600)
    canvas.set_canvas_title("Mystery Square")
    x1 = 200
    y1 = 100
    rect = canvas.create_rectangle(x1, y1, x1 + SQUARE_SIZE, y1 + SQUARE_SIZE)
    while True:
        colour = canvas.get_random_color()
        canvas.set_color(rect, colour)

        canvas.update()
        time.sleep(DELAY)
    canvas.mainloop()


if __name__ == "__main__":
    main()
