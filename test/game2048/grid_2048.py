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
    empty_cases_coordinates = [(i,j) for i in range(len(game_grid)) for j in range(len(game_grid)) if game_grid[i][j] == '']


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
    L = [[[0] *len(game_grid)] * len(game_grid)]
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            if game_grid[i][j] == '':
                L.append(0)
            else : 
                L.append(game_grid[i][j])
                           
    return game_grid

    

    



def get_value_new_tile(): 
        #we initiate the value with 0
        tile_value = 0

        # Si la valeur est inférieure à 0.9, choisir la tuile 2
        rand_val = random.random()
        if rand_val < 0.9:
            tile_value= 2
        
        # Si la valeur est supérieur à 0.2, choisir la tuile 4
        else:
            tile_value = 4








