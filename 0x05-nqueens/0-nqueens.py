#!/usr/bin/python3
"""Solves the N Queens problem"""

import sys


def print_usage_and_exit(msg, code=1):
    print(msg)
    sys.exit(code)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[], solutions=[]):
    if row == n:
        solutions.append([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = []
    solve_nqueens(n, 0, [], solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
