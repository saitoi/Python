import sys

def get_int():
    while True:
        try:
            a = int(input("Please enter a number: "))
            return a
        except ValueError:
            print("The number is not valid! Try again..")
        except EOFError:
            sys.exit(1)
try:
    print("Result is", get_int()/get_int())
except ZeroDivisionError:
    print("Program is not able to divide the number by zero..")
