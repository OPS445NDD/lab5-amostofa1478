#!/usr/bin/env python3
# Author ID: amostofa

def read_file_string(file_name):
    # Opens file_name, returns entire contents as one string
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    # Opens file_name, returns lines as a list WITHOUT newline characters
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    lines = data.split('\n')
    # Remove empty string that split() adds at the end
    if lines[-1] == '':
        lines = lines[:-1]
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
