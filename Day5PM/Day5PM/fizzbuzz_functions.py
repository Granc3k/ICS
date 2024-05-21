"""
File: fizzbuzz_functions.py
--------------------
This program plays the game fizzbuzz up to a given number entered by the user.
"""


def main():
    num = int(input("Number to count to: "))
    num_fizzbuzzed = fizzbuzz(num)
    print(num_fizzbuzzed, " numbers were Fizzed or buzzed")
def fizzbuzz(n):
    count = 0
    for i in range(n):
        if divisible(i+1, 3) and divisible(i+1, 5):
            print("FizzBuzz")
            count += 1
        elif divisible(i+1, 5):
            print("Buzz")
            count += 1
        elif divisible(i+1, 3):
            print("Fizz")
            count += 1
        else:
            print(i+1)
    return count


def divisible(i, j):
    if i % j == 0:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
