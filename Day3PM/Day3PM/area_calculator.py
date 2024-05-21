"""
File: area_calculator.py
-------------------
This program can calculate the area of a circle with a radius that
is entered by the user.  It also prints out if the user has entered
an invalid (0 or negative) radius.
"""

# This line is needed to use the value of pi
import math


def main():
    # Your code here
    # Delete the `pass` line before starting to write your own code
    while True:
        print()
        radius = int(input(" Please enter a circle radius: "))
        if radius > 0 :
            solution = math.pi * radius * radius
            print()
            print(" The area of circle is: " + str(solution))
        else:
            print()
            print(" Error! You entered invalid radius. ")

if __name__ == '__main__':
    main()
