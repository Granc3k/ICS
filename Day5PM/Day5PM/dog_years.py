"""
File: dog_years.py
--------------------
This program prints out the number of dog years for a given number
of human years.
"""

DOG_YEARS_PER_HUMAN_YEAR = 7
def main():
    user_input = int(input("Enter an age in human years: "))
    while user_input != 0:
        if user_input < 0:
            print("Sorry, please enter a positive number or 0 to exit")
        else:
            result = compute_dog_years(user_input)
            print("The age in dog years is: ", result)
        user_input = int(input("Enter an age in human years: "))


def compute_dog_years(human_years):
    human_years = human_years * DOG_YEARS_PER_HUMAN_YEAR
    return human_years


if __name__ == "__main__":
    main()
