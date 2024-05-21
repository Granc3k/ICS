"""
File: polka_dot.py
-------------------
This is a program that adds a circle to the canvas when the user clicks
the mouse.  The circle is always added at the same location.
"""

from graphics import Canvas

CIRCLE_SIZE = 25


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Polka Dot")

    while True:
        clicks = canvas.get_new_mouse_clicks()

        # Add a circle each time the user clicks
        for click in clicks:
            circle = canvas.create_oval(0, 0, CIRCLE_SIZE, CIRCLE_SIZE)
            canvas.set_color(circle, 'blue')
        canvas.update()

    canvas.mainloop()


if __name__ == "__main__":
    main()
