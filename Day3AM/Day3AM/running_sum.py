"""
File: running_sum.py
-------------------
This program reads in integers from the user
and then keeps outputting the sum of the entered values.
"""


def main():
    sum = 0
    count = 0
    while True:
        print(" Enter integers, one at a time. I will show you the sum! ")
        num = int(input(" Please enter an integer: "))
        sum = sum + num     #sum changes-depends on inputed number
        count = count + 1   #count changes +1 (everytime
        print()
        print(" The sum is: " + str(sum) + " ( " + str(count) + " integers enterned) ")
        print()

if __name__ == '__main__':
    main()
