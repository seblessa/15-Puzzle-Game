# transforms the matrix to an array
def get_array(matrix):
    board = []
    for line in range(4):
        for column in range(4):
            board.append(matrix[line][column])
    return board


# transforms the array to a matrix
def array_to_matrix(board):
    matrix = [[" ", " ", " ", " "],
              [" ", " ", " ", " "],
              [" ", " ", " ", " "],
              [" ", " ", " ", " "]]
    count = 0
    for line in range(4):
        for column in range(4):
            matrix[line][column] = board[count]
            count += 1
    # printing
    # code to print matrix
    return matrix
