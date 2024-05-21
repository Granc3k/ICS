"""
File: sorted_numbers.py
-------------------
This program prompts the user for 10 numbers, and then
prints out those numbers in sorted order.
"""
numbers = 10


def main():
    my_list = []
    for i in range(numbers):
        number = int(input('>'))
        my_list.append(number)
    my_list.sort()
    for i in range(len(my_list)):          #for elem in my_list:
        print(my_list[i])                       #print(elem)


if __name__ == '__main__':
    main()
