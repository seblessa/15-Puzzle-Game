import heapq
from collections import deque
from operators import moves


# DFS algorithm, using a stack.
def DFS(initial, final, depth_limit):
    stack = [(initial, 0, [initial])]
    visited = set()
    max_nodes = 0
    while stack:
        max_nodes = max(max_nodes, len(stack))
        cur, cur_depth, path = stack.pop()
        if cur == final:
            return max_nodes, path
        if cur_depth < depth_limit:
            for move in moves(cur):
                if str(move) not in visited:
                    visited.add(str(cur))
                    stack.append((move, cur_depth + 1, path + [move]))
    return None, None



# BFS algorithm, using a queue of list of matrices. Each list contains every path possible
# and when one of the paths reach the solution then that path gets returned along with the number of max nodes in the queue,
# isto é, the max number of lists(paths) simultaneously in the queue.
def BFS(initial, final):
    visited = set()
    queue = deque([(initial, [initial])])
    max_nodes = 0
    while len(queue):
        max_nodes = max(len(queue), max_nodes)
        cur, path = queue.popleft()
        if cur == final:
            return max_nodes, path
        for move in moves(cur):
            if str(move) not in visited:
                queue.append((move, path + [move]))
                visited.add(str(move))


# Greedy algorithm using a heap. It starts pushing the heap with a tuple containing the heuristic,inicial state and a list of the path.
# Then it gets popped, checks if the final state is reached, checks if the state has already been visited and then
# if neither of those is confirmed it checks the possible moves, and then
# it pushes a tuple containing the heuristic of the current state, each move, and the path + each move (so that the path in each tuple is preserved).
# Now it has pushed into the heap the possible moves along with the other stuff, and  it's ready
def greedy(initial, final, h):
    heap = [(h(initial, final), initial, [initial])]
    heapq.heapify(heap)
    visited = set()
    max_nodes = 0
    while heap:
        max_nodes = max(max_nodes, len(heap))
        h_value, cur, path = heapq.heappop(heap)  # Get the board with the lowest heuristic value
        if cur == final:
            return max_nodes, path
        for move in moves(cur):
            if str(move) not in visited:
                visited.add(str(move))
                heapq.heappush(heap, (h(move, final), move, path + [move]))


# Astar Algorith has the same logic of the greedy, except that when calculating the heuristic and pushing it,
# it also adds the length of the path, meaning that the best heuristic is influenced also by the lenght of the path.
# This means that it will choose the best heuristic with the shortest path.
def Astar(initial, final, h):
    heap = [(h(initial, final), initial, [initial])]
    heapq.heapify(heap)
    visited = set()
    max_nodes = 0
    while heap:
        max_nodes = max(max_nodes, len(heap))
        h_value, cur, path = heapq.heappop(heap)  # Get the state with the lowest heuristic value
        if cur == final:
            return max_nodes, path
        for move in moves(cur):
            if str(move) not in visited:
                visited.add(str(move))
                heapq.heappush(heap, (h(move, final) + 1 + len(path), move, path + [move]))


# IDFS algorithm, it uses a list of a tuple containing the current state, the depth, and a list containing the current path.
# it adds to the stack the inicial tuple and then in the beginning of the while it pops it and saves the tuple.
# Runs through the if's to see if it has reached it's final state or if it has been there before(if it's in the visited set). And
# checking if the depth is lower than the limit. If it is, it generates the next possible moves and repeats the process.
# When it's done it repeats the same thing but with a different depth to check the sons of the checked nodes.
# Basically doing a DFS and a BFS at the same time. It then returns a list containing the path from the initial state to the last and the mo
def IDFS(initial, final, depth_limit):
    for depth in range(depth_limit + 1):
        max_nodes, path = DFS(initial, final, depth)
        if path is not None:
            return max_nodes, path
