#!/usr/bin/env python3
# Author ID: [wcao23]

def read_file_string(file_name):
    f = open(file_name, 'r')
    file = f.read()
    f.close()
    return str(file)
    
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open(file_name, 'r')
    file_list = f.readlines()
    f.close()
    return [line.strip() for line in file_list]       
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))