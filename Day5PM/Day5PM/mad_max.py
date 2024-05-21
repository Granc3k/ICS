"""
File: mad_max.py
--------------------
This program can print out the maximum of numbers.
"""


def main():
    print("The max of 4, 5, and 6 is:", mad_max(4, 5, 6))
    print("The max of -4, 4, and 0 is:", mad_max(-4, 4, 0))
    print("The max of 3, 2, and 1 is:", mad_max(3, 2, 1))
    print("The max of 0, 0, and 0 is:", mad_max(0, 0, 0))


def mad_max(x, y, z):
    if x > y:
        if x > z:
            return x
    elif z > y:
        if z > x:
            return z
    return y


if __name__ == "__main__":
    main()
