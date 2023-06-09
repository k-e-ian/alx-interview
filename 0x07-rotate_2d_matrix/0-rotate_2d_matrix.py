#!/usr/bin/python3.8
'''
File: 0-rotate_2d_matrix.py
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate matrix 9- degrees
    '''
    n = len(matrix)  # Get the size of the matrix

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
