#!/usr/bin/python3
"""
Title: 101-nqueens.py
Description: The N queens puzzle is the challenge of placing N non-attacking
        queens on an N×N chessboard. Write a program that solves the N queens
        problem
Author: @a_idk Scripting
"""
import sys


def init_chessboard(n):
    """
    Initializing the chessboard

    Args:
        n: number of pieces
    """
    chess_board = []  # initializing the list
    [chess_board.append([]) for x in range(n)]
    [row.append(' ') for y in range(n) for row in chess_board]
    return chess_board


def board_dcopy(chess_board):
    """
    Returns deepcopy of chessboard
    Args:
        chess_board: The chess board
    """
    if isinstance(chess_board, list):
        return list(map(board_dcopy, chess_board))
    return chess_board


def get_soln(chess_board):
    """
    Return the list of lists representation of a solved chessboard
    """
    soln = []
    for row in range(len(chess_board)):
        for col in range(len(chess_board)):
            if chess_board[row][col] == "Q":
                soln.append([row, col])
                break
    return soln


def markout(chess_board, row, col):
    """
    Mark out spots on a chessboard for non attacking queen
    Args:
        chess_board: the board under consideration
        row: row on chessboard previously used by queen
        col: col previously used by queen
    """

    # marking forward and backward column spots
    for x in range(col + 1, len(chess_board)):
        chess_board[row][x] = "x"
    for x in range(col - 1, -1, -1):
        chess_board[row][x] = "x"

    # marking spots for row above and below
    for y in range(row + 1, len(chess_board)):
        chess_board[y][col] = "x"
    for y in range(row - 1, -1, -1):
        chess_board[y][col] = "x"

    # marking right and left diagonal spots
    x = col + 1
    for y in range(row + 1, len(chess_board)):
        if x >= len(chess_board):
            break
        chess_board[y][x] = "x"
        x = x + 1

    x = col - 1
    for y in range(row - 1, -1, -1):
        if x < 0:
            break
        chess_board[y][x]
        x = x - 1
    # marking out all diagonal spot up to right and down to left
    x = col + 1
    for y in range(row - 1, -1, -1):
        if x >= len(chess_board):
            break
        chess_board[y][x] = "x"
        x = x + 1
    x = col - 1
    for y in range(row + 1, len(chess_board)):
        if x < 0:
            break
        chess_board[y][x] = "x"
        x = x - 1


def r_solve(chess_board, row, queens, solns):
    """
    Recursive solution to N-queens puzzle.
    Args:
        chess_board: chess board under consideration
        row: active row
        queens: placed queens
        solns: possible  results
    """
    if queens == len(chess_board):
        solns.append(get_soln(chess_board))
        return solns

    for c in range(len(chess_board)):
        if chess_board[row][c] == " ":
            temp_board = board_dcopy(chess_board)
            temp_board[row][c] = "Q"
            markout(temp_board, row, c)
            solns = r_solve(temp_board, row + 1, queens + 1, solns)
    return solns


if __name__ == "__main__":
    # checking for wrong no. of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # check for N as integer
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    # check for N < 4
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    chess_board = init_chessboard(int(sys.argv[1]))
    solns = r_solve(chess_board, 0, 0, [])
    for x in solns:
        print(x)
