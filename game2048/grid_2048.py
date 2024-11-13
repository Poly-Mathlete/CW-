import random


def create_grid(n=4):
    game_grid = []
    for i in range(0,n):
        game_grid.append([' ' for i in range(n)])
    return game_grid


def get_all_tiles(grid):
    L = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j] == ' ':
                L+= [0]
            else : L+= [grid[i][j]]
    return L

def get_value_new_tile():
    t = random.choice([1,2,3,4,5,6,7,8,9,10])
    if t == 10 :return 4
    return 2

def get_empty_tiles_positions(grid):
    L = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] in {' ',0}:
                L+= [(i,j)]
    return L

def get_new_position(grid):
    L = get_empty_tiles_positions(grid)
    return random.choice(L)

def grid_get_value(grid,a,b):
    if grid[a][b] == ' ' : return 0
    return grid[a][b]


def grid_add_new_tile(grid,x=None,y=None):
    if x is not None and y is not None:
        t = random.choice([1,2,3,4,5,6,7,8,9,10])
        if t == 10 : grid[x][y] = 4
        else : grid[x][y] = 2
        return grid
    else :
        (x,y) = get_new_position(grid)
        grid = grid_add_new_tile(grid,x,y)
        return grid

def init_game(n=4):
    grid = create_grid(n)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid