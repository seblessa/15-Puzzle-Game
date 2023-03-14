import random
from solvers import solvable


# For the algorithms, returns a list('moves_possible') with all the possible successors of 'matrix'.
# If there isn't a successor for one of the sides, it doesn't get added into the list
def moves(matrix):
    moves_possible = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "0":
                if i > 0:
                    new_matrix = [r[:] for r in matrix]
                    new_matrix[i][j], new_matrix[i - 1][j] = new_matrix[i - 1][j], new_matrix[i][j]
                    moves_possible.append(new_matrix)
                if i < 3:
                    new_matrix = [r[:] for r in matrix]
                    new_matrix[i][j], new_matrix[i + 1][j] = new_matrix[i + 1][j], new_matrix[i][j]
                    moves_possible.append(new_matrix)
                if j > 0:
                    new_matrix = [r[:] for r in matrix]
                    new_matrix[i][j], new_matrix[i][j - 1] = new_matrix[i][j - 1], new_matrix[i][j]
                    moves_possible.append(new_matrix)
                if j < 3:
                    new_matrix = [r[:] for r in matrix]
                    new_matrix[i][j], new_matrix[i][j + 1] = new_matrix[i][j + 1], new_matrix[i][j]
                    moves_possible.append(new_matrix)
                return moves_possible


# Finds the zero (empty space) coordinates
def zero_coordinates(matrix):
    for line in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[line][column] == "0":
                return line, column  # zero's coordinates


# checks whether the position 'x' is within the board
def check(x):
    if 0 <= x[0] <= 3 and 0 <= x[1] <= 3:
        return True
    return False


# Creates a board, randomly or from input
def create_board():
    board = []
    print("Input the initial state - press 1")
    print("Randomized initial state - press 2")
    n = input("Selected option: ")
    while n != "1" and n != "2":
        n = input("Invalid option, choose again:")
    if n == "2":
        board = random_board()
    elif n == "1":
        board = input_board()
    return board


# generate random board
def random_board():
    board = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0".split()
    random.shuffle(board)
    while not solvable(board):
        board = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0".split()
        random.shuffle(board)
    return board


# input board, given by player
def input_board():
    return input('Please enter 16 numbers from 0 to 15:\n').split()


# input with txt file
def input_text():
    return input().split()


# Print the board
def print_board(board):
    print("")
    count = 0
    for i in range(4):
        row = ""
        for j in range(4):
            row += board[count].rjust(3)
            count += 1
        print(row)
    print("")
