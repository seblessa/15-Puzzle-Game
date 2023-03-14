# Manhattan: |x1 − x2| + |y1 − y2|
# Manhattan distance


def manhattan(initial, final):
    count = 0
    for x in range(4):
        for y in range(4):
            if initial[x][y] != "0":
                xf, yf = find_coordinate(final, initial[x][y])  # find the same number in the other matrix
                count += abs(x-xf) + abs(y-yf)  # count of movements
    return count


# Misplaced
def misplaced(initial, final):
    count = 0
    for x in range(4):
        for y in range(4):
            if initial[x][y] != final[x][y]:
                count += 1
    return count


def find_coordinate(matrix, a):
    a = str(a)
    for x in range(4):
        for y in range(4):
            if matrix[x][y] == a:
                return x, y
