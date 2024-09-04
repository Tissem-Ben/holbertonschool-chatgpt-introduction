#!/usr/bin/python3
import sys
def factorial(n):
        result = 1
        while n > 1:
                result *= n
                n -= 1 # Decrement n to avoid an infinite loop
                return result
                if __name__=="__main__"
                # Check if an argument is passed and calculate the factorial
                if len(sys.argv) != 2:
                        print("usage: ./factorial.py <number>")
                        sys.exit(1)
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
