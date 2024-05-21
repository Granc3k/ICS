"""
File: whack_a_mole.py
-------------------
This is a program that puts random moles on the screen that the
user must click to "whack" and earn points.

Each iteration of the animation loop, there is a small chance that a mole appears somewhere
random on the screen.  If the user clicks a mole, the mole disappears and the user's score,
displayed in the upper-left corner in a label, increases by 1.
The game plays until the user gets a certain number of points.
"""

from graphics import Canvas
import random
import time

WIN_SCORE = 10
NEW_MOLE_CHANCE = 0.02
ANIMATION_DELAY_SECONDS = 0.01


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Whack-A-Mole")

    score = 0
    score_label = add_score_label(canvas, score)
    canvas.update()

    while score < WIN_SCORE:
        # Randomly make a new mole some of the time
        if random.random() <= NEW_MOLE_CHANCE:
            create_mole(canvas)

        score = handle_clicks(canvas, score_label, score)

        canvas.update()
        time.sleep(ANIMATION_DELAY_SECONDS)

    canvas.mainloop()


def add_score_label(canvas, score):
    """
    Adds a score label to the top-left corner of the screen, displaying
    the initial score of 0.
    """
    label = canvas.create_text(0, 0, "")
    canvas.set_font(label, "Courier", 20)
    update_score_label(canvas, label, score)
    return label


def update_score_label(canvas, score_label, score):
    """
    Updates the given score label to display the given score amount,
    and reposition it to make sure it is in the top-left corner (the text
    could be longer with a bigger score, so we must reposition it).
    """
    canvas.set_text(score_label, "Score: " + str(score))

    # Set the top-left corner of this label to be 0, 0
    canvas.moveto(score_label, 0, 0)


def create_mole(canvas):
    """
    Creates a new mole on the canvas at a random location.
    """
    mole = canvas.create_image(0, 0, "mole.png")
    x = random.randint(0, canvas.get_canvas_width() - canvas.get_width(mole))
    y = random.randint(0, canvas.get_canvas_height() - canvas.get_height(mole))
    canvas.moveto(mole, x, y)


def handle_clicks(canvas, score_label, score):
    """
    Handles any clicks that have recently occurred.  For each click,
    we check if it is clicking on a mole, and if it is, remove that
    mole and increment the score by one.  This function returns
    the updated score after handling any clicks.
    """
    # TODO: our code here (remove the line below first)
    return score


if __name__ == "__main__":
    main()
