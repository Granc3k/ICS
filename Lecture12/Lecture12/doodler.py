"""
File: doodler.py
-------------------
This is a program that lets the user "doodle" by drawing rectangles
along the path where the user moves the mouse.
"""

from graphics import Canvas

SQUARE_SIZE = 10


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Doodler")

    while True:
        # Get the mouse location
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Create a black rectangle at this location
        rect = canvas.create_rectangle(mouse_x, mouse_y, mouse_x + SQUARE_SIZE, mouse_y + SQUARE_SIZE)
        canvas.set_color(rect, 'black')

        canvas.update()

    canvas.mainloop()


if __name__ == "__main__":
    main()
