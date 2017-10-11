#!/usr/bin/python -tt

import sys

# Define a main() function that prints a little greeting.

def main():
# Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = input("Wait, what's your name? > ")
    
    print ('Hello', name)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()