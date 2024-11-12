import random

def valeur_aleatoire(liste):
    return random.choice(liste)


def create_grid(n=4):
    game_grid = []
    for i in range(0,n):
        game_grid.append([' ' for i in range(n)])
    return game_grid

def grid_add_new_tile_at_position(grid,a,b):
    t = random.choice([1,2,3,4,5,6,7,8,9,10])
    assert a,b in [i for i in range(n)]
    if t == 10 : grid[a][b] = 4
    else : grid[a][b] = 2
    return grid

def get_all_tiles(grid):
    L = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j] == ' ':
                L+= [0]
            else : L+= [grid[i][j]]
    return L

def get_value_new_tile():
    return 2