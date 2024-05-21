"""
File: polka_dot_2.py
-------------------
This is a program that adds a circle to the canvas wherever the user
clicks the mouse.
"""

from graphics import Canvas

CIRCLE_SIZE = 25


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Polka Dot 2")

    while True:
        clicks = canvas.get_new_mouse_clicks()

        # Add a circle each time the user clicks
        for click in clicks:
            circle = canvas.create_oval(click.x, click.y,
                                        click.x + CIRCLE_SIZE,
                                        click.y + CIRCLE_SIZE)
            canvas.set_color(circle, 'blue')
        canvas.update()

    canvas.mainloop()


if __name__ == "__main__":
    main()
