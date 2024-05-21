"""
PyCharm Introduction
"""

import sys
import platform


def main():
    # Check Python version
    if platform.python_version() != "3.8.1":
        print("ERROR: You are not using Python 3.8.1! You are using version: " + platform.python_version())
        print("Please follow the instructions on the course website to download python version 3.8.1")
        return

    # Check if the user entered their name
    if len(sys.argv) != 2:
        print("Hello, world! Now, try running 'python3 intro.py <YOUR NAME HERE>' in the terminal! "
              "(For Windows, use 'py' instead of 'python3')")
    else:
        name = " ".join(sys.argv[1:])
        print("Hello, " + name + "! You're done with the PyCharm setup process!")


# This provided line is required at the end of a Python file to call the main() function.
if __name__ == '__main__':
    main()
