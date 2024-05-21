"""
File: short_film.py
----------------
Creates a short animated film with a sunset to start off with.
"""

from graphics import Canvas
import time
import random

SUN_RADIUS = 25

# The amount the sun should move down the screen each frame
DESCENT = 2
# in seconds
DELAY = 0.03
CANVAS_HEIGHT = 720
CANVAS_WIDTH = 1280
num_rocks = 30
TIME = 4
HALF_WIDTH = CANVAS_WIDTH / 2
HALF_HEIGHT = CANVAS_HEIGHT / 2
s_height = HALF_HEIGHT/2 - SUN_RADIUS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Short Film")
    intro(canvas)
    sun_scenario(canvas)
    end(canvas)
    canvas.mainloop()



def intro(canvas):
    canvas.set_canvas_background_color("black")
    label = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, "Once upon a time...")
    canvas.set_fill_color(label, "white")
    canvas.set_font(label, "Papyrus", 40)
    canvas.update()
    time.sleep(2)
    canvas.delete(label)

def sun_scenario(canvas):
    sky = canvas.create_rectangle(0,0,CANVAS_WIDTH,HALF_HEIGHT)
    sun = canvas.create_oval(HALF_WIDTH-SUN_RADIUS,HALF_HEIGHT/2 - SUN_RADIUS,HALF_WIDTH+SUN_RADIUS,HALF_HEIGHT/2 + SUN_RADIUS)
    for i in range(num_rocks):
        rock(canvas)
    ground = canvas.create_rectangle(0,HALF_HEIGHT,CANVAS_WIDTH,CANVAS_HEIGHT)
    canvas.set_color(sky,"blue")
    canvas.set_color(ground, "green")
    canvas.set_color(sun, "yellow")
    canvas.update()
    time.sleep(TIME)
    count = 0
    while count < s_height:
        canvas.update()
        sun_move(canvas, sun)
        count += DESCENT
    count = 0
    while count < SUN_RADIUS:
        canvas.update()
        canvas.set_fill_color(sun, 'orange')
        sun_move(canvas, sun)
        count += DESCENT
    count = 0
    while count < SUN_RADIUS:
        canvas.update()
        canvas.set_fill_color(sun, 'red')
        sun_move(canvas, sun)
        count += DESCENT
    time.sleep(DELAY)
    canvas.update()

def sun_move(canvas, sun):
    canvas.move(sun, 0, DESCENT)
    canvas.update()
    time.sleep(DELAY)

def rock(canvas):
    num_r = random.randint(0, SUN_RADIUS)
    x1 = random.randint(0, CANVAS_WIDTH-SUN_RADIUS)
    y1 = HALF_HEIGHT - num_r
    y2 = HALF_HEIGHT + num_r
    x2 = x1 - SUN_RADIUS
    stone = canvas.create_oval(x1,y1,x2,y2)
    canvas.set_fill_color(stone,"gray")

def end(canvas):
    rect = canvas.create_rectangle(0,0,CANVAS_WIDTH,CANVAS_HEIGHT)
    canvas.set_fill_color(rect, "black")
    label = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, "That s the END...")
    canvas.set_fill_color(label, "white")
    canvas.set_font(label, "Papyrus", 40)

if __name__ == '__main__':
    main()
