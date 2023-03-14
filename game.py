from operators import print_board, check, zero_coordinates
import main
from time import time
from transformers import *


# Plays the game
def play_game(board):
    ti = time()
    matrix = array_to_matrix(board)

    while True:
        print("\nWhere do you want to move the empty space!")

        print_board(get_array(matrix))

        print("Up - press w")
        print("Down - press s")
        print("Left - press a")
        print("Right - press d")

        direction = get_direction(input("\nMove: "))
        while direction != "up" and direction != "down" and direction != "left" and direction != "right":
            direction = get_direction(input("Invalid move, try again!\n"))

        matrix = move(matrix, direction)

        if win(matrix, [["1", "2", "3", "4"],
                        ["5", "6", "7", "8"],
                        ["9", "10", "11", "12"],
                        ["13", "14", "15", "0"]]):
            break

    tf = time()

    print("You won the game in " + str(round(tf - ti, 3)) + " seconds.")

    board = get_array(matrix)
    main.menu(board)


# to improve the gameplay this functions is added receive a letter and then translates to a direction
def get_direction(m):
    if m == "w":
        return "up"
    elif m == "s":
        return "down"
    elif m == "a":
        return "left"
    elif m == "d":
        return "right"
    return " "


# checks if the matrix is in the 'final' state.
def win(matrix, final):
    if matrix == final:
        return True
    return False


# changes the board with the move that the player made
def board_change(matrix, x, y):
    new_matrix = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    zero = zero_coordinates(matrix)
    # Swap the empty tile with the tile being swapped
    new_matrix[x][y], new_matrix[zero[0]][zero[1]] = new_matrix[zero[0]][zero[1]], new_matrix[x][y]

    return new_matrix


# For the gameplay, returns a board with the zero swapped with the next piece in the direction received.
# If there isn't a successor for one of the sides, it returns the board received.
def move(matrix, direction):
    zero = zero_coordinates(matrix)

    if direction == "up":
        up = (zero[0] + 1, zero[1])
        if check(up):
            return board_change(matrix, up[0], up[1])
        else:
            return matrix

    elif direction == "down":
        down = (zero[0] - 1, zero[1])
        if check(down):
            return board_change(matrix, down[0], down[1])
        else:
            return matrix

    elif direction == "left":
        left = (zero[0], zero[1] + 1)
        if check(left):
            return board_change(matrix, left[0], left[1])
        else:
            return matrix

    elif direction == "right":
        right = (zero[0], zero[1] - 1)
        if check(right):
            return board_change(matrix, right[0], right[1])
        else:
            return matrix

    else:
        return matrix
