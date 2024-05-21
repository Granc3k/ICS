"""
File: programming_is_awesome.py
--------------------
This program draws various art on the canvas using graphics!
"""

from graphics import Canvas


def main():

    canvas = Canvas(1280, 720)
    canvas.set_canvas_title("Programming is Awesome!")
    label = canvas. create_text( 640, 360, " Programming is awesome! ")
    canvas.set_font(label, "Courier", 50)
    rect_1 = canvas.create_rectangle(100, 100, 50, 50)
    rect_2 = canvas.create_rectangle(800, 660, 1220, 680)
    rect_3 = canvas.create_rectangle(650, 100, 700, 300)
    canvas.set_color(rect_1, "blue")
    canvas.set_color(rect_2, "red")
    canvas.set_color(rect_3, "yellow")
    canvas.mainloop()


if __name__ == '__main__':
    main()
