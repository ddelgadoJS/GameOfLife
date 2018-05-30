# Input: grid with organisms.
# Prints grid to console.
def paintGrid(grid):
    print("---")
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end = ' ')
        print()
