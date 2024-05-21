"""
File: short_film.py
----------------
Creates a short animated film with a sunset to start off with.
"""

from graphics import Canvas
import time

SUN_RADIUS = 25

# The amount the sun should move down the screen each frame
DESCENT = 2

# in seconds
DELAY = 0.03
CANVAS_HEIGHT = 720
CANVAS_WIDTH = 1280
HALF_WIDTH = CANVAS_WIDTH/2
y = CANVAS_HEIGHT/4


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Short Film")
    create_intro()
    sun_scenario()



    canvas.mainloop()

def get_sun_color(color):





def create_intro():
    canvas.set_canvas_background_color("black")
    label = canvas.create_text(HALF_WIDTH, CANVAS_HEIGHT / 2, "Once upon a time...")
    canvas.set_font(label, "Papyrus", 40)
    canvas.set_color(label, 'white')
    time.sleep(2)
    canvas.delete(label)
    canvas.delete(rect)

def sun_scenario():
    sky = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT / 2)
    ground = canvas.create_rectangle(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_color(sky, 'blue')
    canvas.set_color(ground, 'green')
    sun = canvas.create_oval(HALF_WIDTH - SUN_RADIUS, y, HALF_WIDTH + SUN_RADIUS, y + SUN_RADIUS)



if __name__ == '__main__':
    main()
