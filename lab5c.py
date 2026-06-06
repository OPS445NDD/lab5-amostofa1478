#!/usr/bin/env python3
# Author ID: amostofa

def add(number1, number2):
    # Tries to add two numbers; if it fails returns error string
    try:
        return int(number1) + int(number2)
    except:
        return 'error: could not add numbers'

def read_file(filename):
    # Tries to read file; if it fails returns error string
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))               # works → 15
    print(add('10', 5))             # works → 15
    print(add('abc', 5))            # exception → error message
    print(read_file('seneca2.txt')) # works → list of lines
    print(read_file('file10000.txt')) # exception → error message
