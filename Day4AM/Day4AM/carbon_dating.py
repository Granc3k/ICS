"""
File: carbon_dating.py
------------------
This program runs carbon dating (how cool!)
First, it prints out a lookup table that maps the percent
of c14 remaining to the number of years the sample has been
dead for, for the first 20 half lives.

Then, it prompts the user to enter a percent of c14, and it
will output the age of that sample.  It will re-prompt the user
until they enter -1, at which point the program will terminate.
"""

import math

def main():

    MAX = 0
    years = 0
    C14_HALF_LIFE = 5700
    percent = 100.0
    print( "Carbon Dating Lookup Table")
    print(" Percent C-14 Remaining : years passed ")
    print("---------------------------------------")
    for i in range(20):
        print(str(percent) + " %: " + str(years) + "years")
        percent /= 2
        years += int(C14_HALF_LIFE)
    print(str(percent) + " %: " + str(years) + "years") #table for start
    while True:
        print()
        num = float(input("What percent of natural carbon-14 does your sample have? "))
        if num > MAX:
            p_end = math.log(num/100)
            age = p_end / math.log(0.5) * 5700 #age of the sample
            print(str(num) + " carbon-14....")
            print("Your sample is " + str(age) + " years old. ")
        else:
            print()
            print("Invalid percentage, try again.")





if __name__ == '__main__':
    main()
