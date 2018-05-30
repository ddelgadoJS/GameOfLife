from random import randint

# Input: rows of grid, columns of grid.
# Output: list of desired size, with random life organisms.
# Creates array to contain the organisms.
def createGrid(rows, columns):
    grid = [[0 for i in range(rows)] for j in range(columns)]

    for i in range(0, rows):
        for j in range(0, columns):
            grid[i][j] = randint(0, 1)

    return grid

# Input: last generation grid.
# Output: new generation grid.
# Updates the grid with next generation.
def newGeneration(grid):
    newGrid = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            newGrid[i][j] = checkLife(i, j, grid)

    return newGrid

# Input: organism to check.
# Output: state of organism.
# Checks if organism will be alive or dead in the next generation.
def checkLife(i, j, grid):
    leftColumn, rightColumn, upRow, downRow = 0, 0, 0, 0
    neighbors = 0

    # The grid is circular.
    # If organism is in column 0, left column is last.
    if j - 1 < 0: leftColumn = len(grid[0]) - 1
    else: leftColumn = j - 1

    # If organism is in last column, right column is 0.
    if j + 1 == len(grid): rightColumn = 0
    else: rightColumn = j + 1

    # If organism is in first row, up column is last.
    if i - 1 < 0: upRow = len(grid) - 1
    else: upRow = i - 1

    # If organism is in last row, down row is 0.
    if i + 1 == len(grid): downRow = 0
    else: downRow = i + 1

    # Checking neighbors.
    # IMPROVE THIS
    if grid[upRow][leftColumn] == 1: neighbors += 1
    if grid[upRow][j] == 1: neighbors += 1
    if grid[upRow][rightColumn] == 1: neighbors += 1
    if grid[i][leftColumn] == 1: neighbors += 1
    if grid[i][rightColumn] == 1: neighbors += 1
    if grid[downRow][leftColumn] == 1: neighbors += 1
    if grid[downRow][j] == 1: neighbors += 1
    if grid[downRow][rightColumn] == 1: neighbors += 1

    # Checking alive cell.
    # 1. Any live cell with fewer than two live neighbors dies, as if by under population.
    # 2. Any live cell with two or three live neighbors lives on to the next generation.
    # 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    if grid[i][j] == 1:
        if neighbors < 2: return 0
        elif neighbors > 3: return 0
        else: return 1
    # Checking dead cell.
    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    else:
        if neighbors == 3: return 1
        else: return 0
