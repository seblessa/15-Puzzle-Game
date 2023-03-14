import sys
from time import time
import operators
import solvers
from game import play_game
from algorithm import *
from heuristic import *
from transformers import *


MAX_DEPTH = 25

def intro():
    print("How do you want to play ?")
    board = operators.create_board()
    menu(board)


def print_path(path):
    count = 0
    for m in path:
        print("    "+str(count)+" moves")
        count += 1
        operators.print_board(get_array(m))
        print("-------------------")
        # time.sleep(0.3)


# Main for testing the algorithms
def text(strategy,bool):
    initial = operators.input_text()
    final = operators.input_text()

    def run(strat):
        print("Using " + strat + ":")
        ti = time()
        if strat == "DFS":
            memory, path = DFS(initial, final, MAX_DEPTH)           # when given the previously known pass length it gives good results.
            if path is None:
                 print("No solution found.")
                 exit()
        elif strat == "BFS":
            memory, path = BFS(initial, final)
        elif strat == "IDFS":
            memory, path = IDFS(initial, final, sys.maxsize)
        elif strat == "Greedy-misplaced":
            memory, path = greedy(initial, final, misplaced)
        elif strat == "Greedy-manhattan":
            memory, path = greedy(initial, final, manhattan)
        elif strat == "Astar-misplaced":
            memory, path = Astar(initial, final, misplaced)
        elif strat == "Astar-manhattan":
            memory, path = Astar(initial, final, manhattan)
        else:
            print(
                "Strategy not valid.\n(Available strategies: DFS, BFS,IDFS, Greedy-misplaced, Greedy-manhattan, Astar-misplaced, Astar-manhattan)")
            exit()
        tf = time()
        print("memory: " + str(memory))
        print("path size: " + str(len(path) - 1))
        if bool:
            print_path(path)
        print("time: " + str(round(tf - ti, 9)) + " seconds.\n")

    if solvers.reachable(initial, final):
        initial = array_to_matrix(initial)
        final = array_to_matrix(final)
        run(strategy)
    else:
        print("It is impossible to reach a solution")


def menu(board):
    print("\nWhat do you want to do next with the state ?")
    operators.print_board(board)
    print(
        "See if it's Solvable? - press 1")  # Player wants to check if the initial board can be solved to get to the standard board
    print("Play it! - press 2")
    print("Try to reach a custom state - press 3")  # Player inputs final board
    print("Change the initial state - press 4")
    print("Exit - press 0")
    n = input("\nSelected option: ")
    while n != "0" and n != "1" and n != "2" and n != "3" and n != "4":
        n = input("Invalid option, choose again:")

    if n == "1":
        if solvers.solvable(board):
            print("It's Solvable!")
            print("Number of inversions: " + str(solvers.count_inversions(board)) + "\n")
        else:
            print("It's impossible to solve!\n")
        menu(board)

    elif n == "2":
        play_game(board)
        menu(board)

    elif n == "3":
        print("\nHow do you want to create another state ?")
        final_board = operators.create_board()
        print("\nThe custom state chosen is:")
        operators.print_board(final_board)
        if solvers.reachable(board, final_board):
            print("The custom state IS reachable by the previously state")
        else:
            print("The custom state IS NOT reachable by the previously state")
        menu(board)

    elif n == "4":
        board = operators.create_board()
        menu(board)

    else:
        exit()
