"""
File: bouncing_ball.py
---------------------
This program animates a ball (circle) bouncing around the screen.
"""

from graphics import Canvas

# Needed to place the ball randomly on the canvas.  Don't remove this.
import random

# Needed to delay the animation.  Don't remove this.
import time

# Size of the ball
BALL_RADIUS = 20

# Seconds to pause each animation cycle
DELAY = 0.02

"""
The value of the speed in the x and y direction the ball should travel.
In other words, the ball will be traveling either +5 or -5 in the x direction, and
+5 or -5 in the y direction, at all times.
"""
BALL_SPEED = 5


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Bouncing Ball")

    # TODO: your code here

    canvas.mainloop()


if __name__ == "__main__":
    main()
