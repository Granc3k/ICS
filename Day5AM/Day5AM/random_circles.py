"""
File: random_circles.py
-------------------
Draws 10 random circles such that each circle is on the screen.
"""

from graphics import Canvas
# this is needed to generate random numbers.  Don't delete this.
import random

def main():
    NUM_CIRCLES = 10
    canvas = Canvas(1280, 720)
    canvas.set_canvas_title("Random Circles")

    for i in range(NUM_CIRCLES):
        x1 = random.randint(0, 1080)   #setting up 1st cooardinates
        y1 = random.randint(0, 520)
        radius = random.randint(70, 200)   #value of radius
        x2 = x1 + radius     #counting 2nd cooardinates
        y2 = y1 + radius
        color = canvas.get_random_color()    #setting up colour
        circle = canvas.create_oval(x1, y1, x2, y2)      #drawing circle
        canvas.set_color(circle, color)         #adding colour to circle
        NUM_CIRCLES -= 1           #

    canvas.mainloop()


# call the function
if __name__ == '__main__':
    main()
