import numpy as np
def valid_move (grid,row,col,number):

    for i in range(9):
        if grid[row][i] == number:
            return False

    for i in range(9):
        if grid[i][col] == number:
            return False 

    corner_row = row-row % 3 
    corner_col = col - col % 3
    

    for x in range(3):
         for y in range(3):
           if grid[corner_row+x][corner_col + y] == number:
            return False          

    return True

def solve (grid,row,col):
    if col == 9:
        if row == 8:
            return True 
        row += 1
        col = 0

    if grid[row][col]>0:
        return solve(grid,row,col+1)

    for num in range(1,10):
        if valid_move(grid, row, col, num) :

            grid[row][col] = num

            if solve(grid, row, col+1):
                return True
        grid[row][col] = 0

    return False            


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [ 1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            
            print(np.matrix (grid))
        print()
else:
    print("No result found")                     