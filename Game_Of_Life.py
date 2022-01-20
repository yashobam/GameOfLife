import copy
def count_neighbors(cellc, cellr, grid):
    count = 0
    for r in range(cellr - 1, cellr + 2):
        for c in range(cellc - 1, cellc + 2):
            if (r == cellr) & (c == cellc):
                continue
            else:
                if (grid[r][c] == 1):
                    count += 1
    return count

def print_grid(grid):
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end="  ")
        print() 

def next_gen(grid):
    new_grid=copy.deepcopy(grid)
    height = len(new_grid)
    width = len(new_grid[0])
    for r in range(1, height-1):
        for c in range(1, width-1):
                if grid[r][c]==1:
                    if count_neighbors(c,r,grid)!=2 and count_neighbors(c,r,grid)!=3:
                        new_grid[r][c]= 0 
                else:
                    if count_neighbors(c,r,grid)==3:
                        new_grid[r][c]= 1
    return new_grid

def calling(grid,n):
    print ("Original Grid is:")
    print_grid(grid)
    x=grid
    for i in range(n):
        x=next_gen(x)
    print("The Mutated Grid is:")
    print_grid(x)
calling([[0, 0 ,0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]],1);