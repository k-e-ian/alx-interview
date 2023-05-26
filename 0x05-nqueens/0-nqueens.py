#!/usr/bin/python3
'''
File: 0-nqueens.py
'''

import sys


def is_safe(board, row, col, N):
    '''
    Check if a queen can be placed at board[row][col]
    '''

    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    '''
    Solve the N Queens problem and return all solutions
    '''

    # Initialize an empty N x N board
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(N, 0, board, solutions)
    return solutions


def solve_nqueens_util(N, col, board, solutions):
    '''
    Recursive utility function to solve N Queens problem
    '''

    # Base case: If all queens are placed, store the solution
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Consider this column and try placing a queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(N, col + 1, board, solutions)

            # Backtrack: Remove the queen from board[i][col]
            board[i][col] = 0


def main():
    '''
    Main function to parse command-line arguments and solve N Queens problem
    '''

    # Parse the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    main()
