"""
File: phone_book.py
-----------------
This program allows the user to store and lookup phone numbers
in a phone book.  They can "add", "lookup" or "quit".
"""
import time

def main():
    dict = {}
    print("Welcome to Phone Book! This program stores phone numbers")
    print("of contacts. You can add a new number, a get number,")
    print("or quit ('add', 'lookup', 'quit').")
    print("Enter your command at the prompt.")
    while True:
        command = input("('add', 'lookup', 'quit') > ")
        if command == 'add':
            name = input("Enter the name of the person: ")
            number = input("Enter the phone number of that person: ")
            dict[name] = number
        elif command == 'lookup':
            key_w = input("Whose number do u want to know? ")
            if key_w in dict:
                print(dict[key_w])
            else:
                print("This person is not in this dictionary.")
        elif command == 'quit':
            print("Okay, Goodbye :)")
            time.sleep(5)
            return False
        else:
            print("Your command wasn t recognized. Try again.")

if __name__ == '__main__':
    main()
