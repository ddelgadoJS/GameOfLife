import Algorithm as Al
import Console
import GUI

# Main
grid = Al.createGrid(30, 30)

buttonsGrid = GUI.buttonsGrid(grid)
GUI.openWindow(buttonsGrid, grid)

#for i in range(0, 4):
    #Console.paintGrid(grid)
    #grid = Al.newGeneration(grid)
    #Console.paintGrid(grid)
