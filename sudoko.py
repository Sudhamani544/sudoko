grid= [[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]

def validnum(r,c,n):
  #check row
  for i in range(9):
    if grid[r][i] == n:
      return False
  #check column
  for j in range(9):
    if grid[j][c] == n:
      return False
  #check subgrid
  r0 = r//3 * 3
  c0 = c//3 * 3
  for i in range(3):
    for j in range(3):
      if grid[r0+i][c0+j] == n:
        return False
  return True

def writevalidnum(grid):
  find = find_empty(grid)
  if not find:
    return True
  else:
    r,c = find
  for n in range(1,len(grid)+1):
      if validnum(r,c,n):
        grid[r][c]=n
        if writevalidnum(grid):
          return True
        grid[r][c]=0
  return False

def find_empty(grid):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 0:
        return (r,c)

def print_sudoko(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                 print(grid[i][j])
            else:
                 print(str(grid[i][j]) + " ",end="")

writevalidnum(grid)
print_sudoko(grid)
