"""
File: moon.py
------------------
Converts weight on earth into weight on the moon.
"""


def main():
    while True:
        e_weigth = float(input("Enter your earth weight: "))
        m_weight = e_weigth * 0.165
        print("Your weight on Moon is: " + str(m_weight))
        print()


if __name__ == "__main__":
    main()
