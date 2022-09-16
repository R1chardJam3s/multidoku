#Sudoku Generator Algorithm - based on the one found at www.101computing.net/sudoku-generator-algorithm/
from random import randint, shuffle

#initialise empty  grid

#only works grid of SQUARE_WIDTH * SQUARE_HEIGHT size

SIZE = 6 # total with of the grid
SQUARE_WIDTH = 3 # width of the square within the grid; possible stipulation that WIDTH >= HEIGHT
SQUARE_HEIGHT = 2 # height of the square within the grid

grid = [ [0]*SIZE for i in range(SIZE) ]

#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,SIZE):
      for col in range(0,SIZE):
        if grid[row][col]==0:
          return False

  #We have a complete grid!  
  return True 

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,SIZE * SIZE):
    row=i//SIZE
    col=i%SIZE
    if grid[row][col]==0:
      for value in range (1,SIZE + 1):
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[x_i][col] for x_i in range(0, SIZE)):
            
            #Identify which of the squares we are working on

            square=[]
            square_set = False
            _row_count = 0
            while _row_count < divmod(SIZE,SQUARE_HEIGHT)[0] and not square_set:
              if row<SQUARE_HEIGHT*(_row_count+1):
                _col_count = 0
                while _col_count < divmod(SIZE,SQUARE_WIDTH)[0] and not square_set:
                  if col<SQUARE_WIDTH*(_col_count+1):
                    square=[grid[i][SQUARE_WIDTH*_col_count:SQUARE_WIDTH*(_col_count+1)] for i in range(SQUARE_HEIGHT*(_row_count),SQUARE_HEIGHT*(_row_count+1))]
                    square_set = True
                  _col_count += 1
              _row_count += 1

            #Check that this value has not already be used on this square

            temp = []
            for i in range(0,SQUARE_HEIGHT):
              temp.extend(square[i])

            if not value in (temp):
              grid[row][col]=value
              if checkGrid(grid):
                counter+=1
                break
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col]=0  

numberList=[]
numberList.extend(range(1, SIZE+1))
#shuffle(numberList)

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def fillGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,SIZE*SIZE):
    row=i//SIZE
    col=i%SIZE
    if grid[row][col]==0:
      shuffle(numberList)      
      for value in numberList:
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[x_i][col] for x_i in range(0, SIZE)):

            #Identify which of the squares we are working on

            square=[]
            square_set = False
            _row_count = 0
            while _row_count < divmod(SIZE,SQUARE_HEIGHT)[0] and not square_set:
              if row<SQUARE_HEIGHT*(_row_count+1):
                _col_count = 0
                while _col_count < divmod(SIZE,SQUARE_WIDTH)[0] and not square_set:
                  if col<SQUARE_WIDTH*(_col_count+1):
                    square=[grid[i][SQUARE_WIDTH*_col_count:SQUARE_WIDTH*(_col_count+1)] for i in range(SQUARE_HEIGHT*(_row_count),SQUARE_HEIGHT*(_row_count+1))]
                    square_set = True
                  _col_count += 1
              _row_count += 1

            #Check that this value has not already be used on this 3x3 square

            temp = []
            for i in range(0,SQUARE_HEIGHT):
              temp.extend(square[i])

            if not value in (temp):
              grid[row][col]=value
              if checkGrid(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col]=0             
    
#Generate a Fully Solved Grid
fillGrid(grid)

print("Sudoku Grid Ready - Complete")
for row in grid:
    print(row)

#Start Removing Numbers one by one

#A higher number of attempts will end up removing more numbers from the grid
#Potentially resulting in more difficiult grids to solve!
attempts = 5 
counter=1
while attempts>0:
  #Select a random cell that is not already empty
  row = randint(0,SIZE-1)
  col = randint(0,SIZE-1)
  while grid[row][col]==0:
    row = randint(0,SIZE-1)
    col = randint(0,SIZE-1)
  #Remember its cell value in case we need to put it back  
  backup = grid[row][col]
  grid[row][col]=0
  
  #Take a full copy of the grid
  copyGrid = []
  for r in range(0,SIZE):
     copyGrid.append([])
     for c in range(0,SIZE):
        copyGrid[r].append(grid[r][c])
  
  #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
  counter=0      
  solveGrid(copyGrid)   
  #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
  if counter!=1:
    grid[row][col]=backup
    #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
    attempts -= 1

print("\n\nSudoku Grid Ready - Bare")
for row in grid:
    print(row)