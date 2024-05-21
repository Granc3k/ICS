"""
File: catch_me_if_you_can.py
-------------------
This program draws several black "distractor" squares on the screen, along with a blue square that the user
tries to touch with their mouse.  But whenever the mouse touches the blue square, it moves to
another new random location!
"""

from graphics import Canvas
import random

# The dimensions of each black distractor square
DISTRACTOR_SIZE = 50
SIZE = 2 * DISTRACTOR_SIZE
# The number of black squares on screen
N_DISTRACTORS = 20

# The dimensions of the blue square the user is trying to touch with the mouse
GOAL_SIZE = 50

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Catch Me If You Can")
    sneaky, ran_x, ran_y = add_sneaky(canvas)
    sneaky = add_squares(canvas, N_DISTRACTORS, sneaky)
    goal = 0
    label = canvas.create_text(50, 50, "")
    canvas.set_font(label, "Courier", 20)
    while True:
        sneaky, goal, ran_x, ran_y = handle_input(canvas,label, goal,sneaky, ran_x, ran_y)
    """while goal < GOAL_SIZE:
        sneaky, goal = handle_input(canvas, label, goal, sneaky)

        canvas.update()
    canvas.set_canvas_background_color("black")
    end = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, "U WON! :)")
    canvas.set_fill_color(end, "white")"""
    canvas.update()
    canvas.mainloop()

def add_sneaky(canvas):
    ran_x = random.randint(1, CANVAS_WIDTH - SIZE)
    ran_y = random.randint(1, CANVAS_HEIGHT - SIZE)
    sneaky = canvas.create_rectangle(ran_x, ran_y, ran_x+DISTRACTOR_SIZE, ran_y+DISTRACTOR_SIZE)
    canvas.set_color(sneaky, "blue")
    canvas.update()
    return sneaky, ran_x, ran_y

def add_squares(canvas, N_DISTRACTORS, sneaky):
    for i in range(N_DISTRACTORS):
        ran_x = random.randint(1, CANVAS_WIDTH - SIZE)
        ran_y = random.randint(1, CANVAS_HEIGHT - SIZE)
        squares = canvas.create_rectangle(ran_x, ran_y, ran_x + DISTRACTOR_SIZE, ran_y + DISTRACTOR_SIZE)
        canvas.set_color(squares, "black")
        overlapping_objects = canvas.find_overlapping(ran_x, ran_y, ran_x + DISTRACTOR_SIZE, ran_y + DISTRACTOR_SIZE)
        for overlapping_object in overlapping_objects:
            canvas.lower_behind(squares, sneaky)
        canvas.update()
    return sneaky

def handle_input(canvas, label, goal, sneaky, ran_x, ran_y):
    clicks = canvas.get_new_mouse_clicks()
    canvas.update()
    for click in clicks:
        c_x = click.x
        c_y = click.y
        c_object = canvas.find_element_at(click.x, click.y)
        if sneaky == c_object:
            canvas.delete(sneaky)
            sneaky, ran_x, ran_y = move_sneaky(canvas, sneaky)
            goal += 1
            canvas.set_text(label, "Score:" + str(goal))
    canvas.update()
    return sneaky, goal, ran_x, ran_y

def move_sneaky(canvas, sneaky):
    canvas.delete(sneaky)
    canvas.update()
    ran_x = random.randint(1, CANVAS_WIDTH - SIZE)
    ran_y = random.randint(1, CANVAS_HEIGHT - SIZE)
    sneaky = canvas.create_rectangle(ran_x, ran_y, ran_x + DISTRACTOR_SIZE, ran_y + DISTRACTOR_SIZE)
    canvas.set_color(sneaky, "blue")
    canvas.update()
    return sneaky, ran_x, ran_y

if __name__ == '__main__':
    main()
