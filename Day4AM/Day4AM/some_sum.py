"""
File: some_sum.py
-------------------
This program reads in 10 numbers from the user and prints
out the sum of those 10 numbers.
"""


def main():

    num_end = 0
    count = 0
    MAX = 10

    print(" Enter " + str(MAX) + " nums. I will show u the sum! ")
    for i in range(int(MAX)):
        count += 1
        num = int(input(" Please enter integer number " + str(count) + ": "))  #adding num to the sum
        int(count)
        num_end += num #counting sum

    print(" The sum is: " + str(num_end))


if __name__ == '__main__':
    main()
