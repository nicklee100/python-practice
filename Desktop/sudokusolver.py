import os

cwd = os.getcwd()
filename = cwd + "/sudoku1.txt"

grid = []
l = grid
with open(filename) as f:
    for line in f:
        grid.append([int(i) for i in line.split()])


def printGrid(result):  # prints grid with result
    for i in grid:
        print(i)


def allDifferent1D(l):
    for e in l:
        if e != 0:  # ignores that there are many zeros
            if l.count(e) > 1:  #make sure only has 1 instance of a number
                return False
    return True


def allDifferent2D(l):
    for row in l:
        if not allDifferent1D(row):
            return False
    for c in range(len(l)):
        col = []
        for r in range(len(l)):
            col.append(l[r][c])
        if not allDifferent1D(col):
            return False
    return True


def checkAll3By3s(grid):  #function goes through and assigns numbers in                                   arrays and checks the grid
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            column = []
            column.append(grid[i][j:j + 3])
            column.append(grid[i + 1][j:j + 3])
            column.append(grid[i + 2][j:j + 3])
            w = []
            for k in column:
                for p in k:
                    w.append(p)

            if allDifferent1D(l) == False:
                return False
            else:
                return True


def isValidSudoku(grid):  # Check all rows and columns

    if (not allDifferent2D(grid)):
        return False
    if (not checkAll3By3s(grid)):
        return False
    return True


def complete(grid):  # Tells whether the grid is complete (there are no unfilled cells)
    for i in grid:
        if i.count(0): #count numbers of 0's in i if zero return false value after if does not have to be boolean,
            return False
    return True  # returns true if there are no zeros


def checker():  #function to call checkAll3by3
    if checkAll3By3s(grid):
        return grid
    else:
        return False


def solveSudoku(grid):  #main function to solve
    if complete(grid):
        return grid if isValidSudoku(grid) else None  #checks to make sure the grid is complete to theck, choose A if true B is false
    elif not isValidSudoku(grid):
        return None

    for i in grid: # Iterate over lines
        for b in range(0, 9):  #  iterate over cells in a line
            if i[b] == 0:
                for w in range(1, 10):  # Iterate over possible solutions (numbers) to put in the empty cell
                    if i.count(w) == 0:  #can remove, add W, to check if line is correct, before recusion 
                        i[b] = w  # sets the cell in i[b] to the number
                        c = solveSudoku(grid)
                        if c != None:
                            return c  # recursion!
                i[b] = 0  #  sets b back to 0
                return None  #return none, only happen once it  have done everything

result = solveSudoku(grid)  
if result != None:
    print("The solution is:")
    printGrid(result)       
    if not isValidSudoku(grid):
      print("The solution is invalid")
else:
    print("There is no solution.")

   
