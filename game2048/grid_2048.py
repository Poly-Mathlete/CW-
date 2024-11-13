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

def grid_to_string_with_size(grid,n=4):
    n = len(grid)
    a = ' ==='
    for k in range(n-1):
        a+= ' ==='
    a+= '\n'
    for i in range(n):
        for j in range(n):
            a+= '| ' + str(grid[i][j]) + ' '
        a+= '|\n'

        for l in range(n):
            a+= ' ==='
        a+='\n'
    a+= '   '
    return a

def long_value(grid):
    L = get_all_tiles(grid)
    S = [len(str(L[i])) for i in range(len(grid))]
    return max(S)
    
def long_value_with_theme(grid,d):
    L = get_all_tiles(grid)
    S = [len(d[L[i]]) for i in range(len(L))]
    return max(S)

def grid_to_string_with_size_and_theme(grid,d, n=4):
    n = len(grid)
    m = long_value_with_theme(grid,d)
    a = '===='
    for k in range(n-1):
        a+= '==='
    a+= '\n'
    for i in range(n):
        for j in range(n):
            a+= '|' + d[grid[i][j]]
            k = len(d[grid[i][j]])
            if k!=m :
                for g in range(m-k):
                    a+= ' '
        a+= '|\n='
        for l in range(n):
            a+= '==='
        a+='\n'
    return a[:-1]