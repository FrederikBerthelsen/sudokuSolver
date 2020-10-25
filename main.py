grid = [[5, 0, 0, 0, 0, 0, 4, 2, 0],
        [0, 0, 2, 6, 8, 0, 9, 0, 5],
        [0, 0, 7, 0, 5, 0, 0, 8, 0],
        [0, 8, 5, 4, 0, 9, 1, 0, 0],
        [7, 0, 4, 0, 0, 2, 0, 9, 8],
        [2, 1, 0, 0, 3, 0, 0, 0, 4],
        [4, 7, 0, 8, 0, 1, 2, 0, 0],
        [0, 0, 1, 0, 0, 0, 3, 4, 0],
        [0, 2, 0, 3, 0, 5, 8, 7, 0]]

def solver(grid):
    find = findZero(grid)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if validNumber(grid, row, col, i):
            grid[row][col] = i
            if solver(grid):
                return True
            grid[row][col] = 0
    return False

def validNumber(grid, row, col, n):
    if n in grid[row]:
        return False
    for i in grid:
        if i[col] == n:
            return False
    box_x = row // 3
    box_y = col // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[j][i] == n:
                return False
    return True

def findZero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j

def gridPrint(grid):
    for i in grid:
        print(i)
    print("\n")

gridPrint(grid)
solver(grid)
gridPrint(grid)
