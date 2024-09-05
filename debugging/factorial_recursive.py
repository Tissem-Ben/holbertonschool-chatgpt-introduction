#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input number. Returns 1 if n is 0, 
    otherwise returns n multiplied by the factorial of (n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Check if an argument is passed and calculate the factorial
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: The number must be a non-negative integer.")
            sys.exit(1)
    except ValueError:
        print("Error: The argument must be an integer.")
        sys.exit(1)
        
    f = factorial(number)
    print(f)
