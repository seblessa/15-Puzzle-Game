# Counts the number of inversions in the board
def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        if board[i] != '0':
            for j in range(i, len(board)):
                if board[j] != '0' and int(board[i]) > int(board[j]):
                    inversions += 1
    return inversions


# finds the number of the line that the empty space is in.The result is inversely of the index of the matrix lines
# plus 1.
def get_empty_row(board):
    if ((board.index("0") // 4) + 1) == 1:
        return 4
    elif ((board.index("0") // 4) + 1) == 2:
        return 3
    elif ((board.index("0") // 4) + 1) == 3:
        return 2
    elif ((board.index("0") // 4) + 1) == 4:
        return 1


# returns boolean expression on whether it's solvable
def solvable(board):
    empty_row = get_empty_row(board)
    inversions = count_inversions(board)
    return (inversions % 2 == 0) == (empty_row % 2 == 1)


# returns boolean expression on whether the initial board can reach the final board
def reachable(initial_board, final_board):
    return solvable(initial_board) == solvable(final_board)
