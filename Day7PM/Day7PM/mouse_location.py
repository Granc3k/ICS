"""
File: mouse_location.py
-------------------
This program displays a label in the center of the screen displaying the current mouse coordinates.
"""
import time
from graphics import Canvas
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Mouse Location")
    while True:
        m_x = canvas.get_mouse_x()
        m_y = canvas.get_mouse_y()
        label = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, "(" + str(m_x) + " " + str(m_y) + ")")
        canvas.set_font(label, "Arial", 40)
        canvas.update()
        canvas.delete(label)
    canvas.update()
    canvas.mainloop()



if __name__ == "__main__":
    main()
