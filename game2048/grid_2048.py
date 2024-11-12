from typing import List
import random 


def create_grid():
    
    #here we create an empty the grid
    game_grid:List[List[int]] = [] 
    
    for i in range(0,4): # we make the grid a 4x4 table
        game_grid.append([' ',' ',' ', ' ']) 
    return game_grid


def grid_add_new_tile_at_position(game_grid:List[List[int]]):
    
    # we make a list of the available cases 
    empty_cases_coordinates = [(i,j) for i in range(len(game_grid)) for j in range(len(game_grid)) if game_grid[i][j] == 0]
    

    if empty_cases_coordinates :

        # we chose randomly the postion of the tile
        (x,y) = random.choice(empty_cases_coordinates)

        # we chose randomly between 2 and 4 the value of the tile
        game_grid[x][y] = random.choice([2,4]) 



    







