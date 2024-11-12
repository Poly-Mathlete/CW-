from typing import List
import random 


def create_grid():
    
    #here we create an empty the grid
    game_grid:List[List[int]] = [] 
    
    for i in range(0,4): # we make the grid a 4x4 table
        game_grid.append([' ',' ',' ', ' ']) 
    return game_grid


def grid_add_new_tile_at_position(game_grid:List[List[int]], x , y):
    
    # we make a list of the available cases 
    empty_cases_coordinates = [(i,j) for i in range(len(game_grid)) for j in range(len(game_grid)) if game_grid[i][j] == 0]


    if empty_cases_coordinates :

        # we chose randomly the postion of the tile
        (x,y) = random.choice(empty_cases_coordinates)

        # we chose randomly between 2 and 4 the value of the tile
        rand_val = random.random()
    
        # Si la valeur est inférieure à 0.9, choisir la tuile 2
        if rand_val < 0.9:
            game_grid[x][y] = 2
        else:
            game_grid[x][y] = 4



def get_all_tiles(game_grid:List[List[int]]):

    # we return a list of tiles position
    return [ (i,j) for i in range(len(game_grid)) for j in range(len(game_grid)) if game_grid[i][j] in  {2, 4} ] 



def get_value_new_tile(game_grid:List[List[int]]):
    
    return [ game_grid[i][j] for i,j in get_all_tiles(game_grid=create_grid())]






