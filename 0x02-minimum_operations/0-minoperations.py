#!/usr/bin/python3
'''
File: 0-minoperations.py
'''


def minOperations(n):
    '''
    method that calcs the least no of ope's needed to result exactly n H chars
    '''
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    file_contents = 1

    while file_contents < n:
        if n % file_contents == 0:
            clipboard = file_contents
            operations += 1
        file_contents += clipboard
        operations += 1

    return operations if file_contents == n else 0
