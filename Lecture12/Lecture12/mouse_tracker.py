"""
File: mouse_tracker.py
-------------------
This is a program that tracks the user's mouse with a blue square.
"""

from graphics import Canvas

SQUARE_SIZE = 100


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mouse Tracker")

    # Create the square initially in the top-left corner
    square = canvas.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE)
    canvas.set_color(square, 'blue')

    while True:
        # Get the mouse location
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Move the square to this location
        canvas.moveto(square, mouse_x - SQUARE_SIZE / 2, mouse_y - SQUARE_SIZE / 2)

        canvas.update()

    canvas.mainloop()


if __name__ == "__main__":
    main()
