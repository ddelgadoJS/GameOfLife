import tkinter as tk
import Algorithm as Al

import time

top = tk.Tk()
top.title("Game of Life")
top.geometry("1200x700")

def changeButtonColor(i, j):


    """
    if button.cget('bg') == '#40E0D0':
        button.configure(bg = '#FFFFFF')
    else:
        button.configure(bg = '#40E0D0')
    """

def setButtonColor(organism, button):
    if organism == 1:
        button.configure(bg = '#40E0D0')
    else:
        button.configure(bg = '#FFFFFF')

def buttonsGrid(grid):
    buttonsGrid = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            button = tk.Button(top, bd = 0, bg = '#FFFFFF', activebackground = '#40E0D0',
                          activeforeground = '#40E0D0', height = 1, width = 2,
                          command = lambda: changeButtonColor(i, j))

            setButtonColor(grid[i][j], button)

            buttonsGrid[i][j] = button

    return buttonsGrid

def updateWindow(buttonsGrid, grid):
    grid = Al.newGeneration(grid)

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                buttonsGrid[i][j].configure(bg = '#40E0D0')
            else:
                buttonsGrid[i][j].configure(bg = '#FFFFFF')

    return grid

def openWindow(buttonsGrid, grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            buttonsGrid[i][j].grid(column = i, row = j)

    while True:
        top.update()
        grid = updateWindow(buttonsGrid, grid)
        time.sleep(0.3)

    top.mainloop()
