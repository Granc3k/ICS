"""
File: breakout.py
-----------------
This program implements the game Breakout!  The user controls a paddle
moving horizontally with the mouse, and the user must bounce the ball
to make it collide and remove bricks from the screen.  The user has
3 turns.  If the ball falls below the bottom of the screen, the user
loses a turn.  If the user removes all bricks before their turns
run out, they win!
"""

import math
from graphics import Canvas
import random
import time

"""
Dimensions of the canvas, in pixels
These should be used when setting up the initial size of the game,
but in later calculations you should use canvas.get_canvas_width() and 
canvas.get_canvas_height() rather than these constants for accurate size information.
"""
CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600

# Stage 1: Set up the Bricks

# Number of bricks in each row
NBRICK_COLUMNS = 10

# Number of rows of bricks
NBRICK_ROWS = 10

# Separation between neighboring bricks, in pixels
BRICK_SEP = 4

# Width of each brick, in pixels
BRICK_WIDTH = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)

# Height of each brick, in pixels
BRICK_HEIGHT = 8

# Offset of the top brick row from the top, in pixels
BRICK_Y_OFFSET = 70

# Stage 2: Create the Bouncing Ball

# Radius of the ball in pixels
BALL_RADIUS = 10

# The ball's vertical velocity.
VELOCITY_Y = 6.0

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 60

# Stage 3: Create the Paddle

# Dimensions of the paddle
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10

# Offset of the paddle up from the bottom
PADDLE_Y_OFFSET = 30

# Stage 5: Polish and Finishing Up

# Number of turns
NTURNS = 3

BOUNCE_SOUND = "bounce.au"


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")
    create_squares(canvas)
    paddle = create_paddle(canvas)
    ball = create_ball(canvas)
    dx = random.randint(VELOCITY_X_MIN, VELOCITY_X_MAX)
    dy = VELOCITY_Y
    while True:
        dx, dy = move_ball(canvas, ball, dx, dy,paddle)
        canvas.move(ball,dx ,dy)
        move_paddle(canvas, paddle)
        time.sleep(DELAY)
        canvas.update()
    canvas.mainloop()

def create_squares(canvas):
    count = 0
    for i in range(int(NBRICK_ROWS/2)):
        count += 1
        if count == 1:
            y = BRICK_Y_OFFSET
            color = "red"
            create_row(canvas,color,y)
            canvas.update()
            y = y + BRICK_SEP + BRICK_HEIGHT
            create_row(canvas,color,y)
        elif count == 2:
            y = BRICK_Y_OFFSET + 2 * BRICK_HEIGHT + 2 * BRICK_SEP
            color = "orange"
            create_row(canvas,color,y)
            y = y + BRICK_SEP + BRICK_HEIGHT
            create_row(canvas, color, y)
        elif count == 3:
            y = BRICK_Y_OFFSET + 4 * BRICK_HEIGHT + 4 * BRICK_SEP
            color = "yellow"
            create_row(canvas,color,y)
            y = y + BRICK_SEP + BRICK_HEIGHT
            create_row(canvas, color, y)
        elif count == 4:
            y = BRICK_Y_OFFSET + 6 * BRICK_HEIGHT + 6 * BRICK_SEP
            color = "green"
            create_row(canvas,color,y)
            y = y + BRICK_SEP + BRICK_HEIGHT
            create_row(canvas, color, y)
        else:
            y = BRICK_Y_OFFSET + 8 * BRICK_HEIGHT + 8 * BRICK_SEP
            color = "blue"
            create_row(canvas,color,y)
            y = y + BRICK_SEP + BRICK_HEIGHT
            create_row(canvas, color, y)

def create_row(canvas,color,y):
    x = BRICK_SEP
    y2 = y + BRICK_HEIGHT
    for i in range(NBRICK_COLUMNS):
        x2 = x + BRICK_WIDTH
        square = canvas.create_rectangle(x, y, x2, y2)
        canvas.set_color(square, color)
        x = x + BRICK_WIDTH + BRICK_SEP

def collision(canvas,ball,paddle):
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]
    colliders = canvas.find_overlapping(x1,y1,x2,y2)
    for collider in colliders:
        if collider == ball:
            canvas.update()
            return False
        elif collider == paddle:
            return True
        else:
            canvas.delete(collider)
            canvas.update()
            return True
    canvas.update()

def move_ball(canvas, ball , dx, dy,paddle):
    if collision(canvas,ball,paddle):
        dy *= -1
    elif canvas.get_left_x(ball) <= 1:
        dx *= -1
    elif canvas.get_left_x(ball) >= CANVAS_WIDTH - canvas.get_width(ball) - 1:
        dx *= -1
    if canvas.get_top_y(ball) <= 1:
        dy *= -1
    elif canvas.get_top_y(ball) >= CANVAS_HEIGHT - canvas.get_height(ball) - 1:
        return False
    return dx,dy

def create_ball(canvas):
    x = CANVAS_WIDTH/2 - BALL_RADIUS
    y = CANVAS_HEIGHT/2 - BALL_RADIUS
    ball = canvas.create_oval(x,y,x+2*BALL_RADIUS,y+2*BALL_RADIUS)
    canvas.set_color(ball, "black")
    return ball

def create_paddle(canvas):
    x1 = CANVAS_WIDTH/2 - PADDLE_WIDTH/2
    y1 = CANVAS_HEIGHT - PADDLE_Y_OFFSET - PADDLE_HEIGHT
    paddle = canvas.create_rectangle(x1,y1,x1+PADDLE_WIDTH,y1+PADDLE_HEIGHT)
    canvas.set_fill_color(paddle, "black")
    return paddle

def move_paddle(canvas, paddle):
    x = canvas.get_mouse_x()-PADDLE_WIDTH/2
    y = canvas.get_top_y(paddle)
    if canvas.get_left_x(paddle) <= 0:
        canvas.moveto(paddle,1,y)
    elif canvas.get_left_x(paddle)+PADDLE_WIDTH >= CANVAS_WIDTH:
        canvas.moveto(paddle, CANVAS_WIDTH-PADDLE_WIDTH-1,y)
    else:
        canvas.moveto(paddle,x,y)
    canvas.update()

if __name__ == '__main__':
    main()
