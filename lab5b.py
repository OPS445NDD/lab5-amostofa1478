#!/usr/bin/env python3
# Author ID: amostofa

def read_file_string(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    lines = data.split('\n')
    if lines[-1] == '':
        lines = lines[:-1]
    return lines

def append_file_string(file_name, string_of_lines):
    # Appends a string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Writes each item in the list as its own line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads file 1, writes to file 2 with line numbers prepended (e.g. 1:Line 1)
    lines = read_file_list(file_name_read)
    f = open(file_name_write, 'w')
    line_number = 1
    for line in lines:
        f.write(str(line_number) + ':' + line + '\n')
        line_number += 1
    f.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
