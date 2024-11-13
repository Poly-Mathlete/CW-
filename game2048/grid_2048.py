
import random
from typing import List, Tuple, Optional


def create_grid() -> List[List[Optional[int]]]:
    """
    Crée une grille de jeu 4x4 vide pour le jeu 2048.
    
    Returns:
        List[List[Optional[int]]]: Une liste de listes représentant la grille, initialisée avec des valeurs None.
    """
    return [[None for _ in range(4)] for _ in range(4)]




def grid_add_new_tile_at_position(game_grid: List[List[Optional[int]]], x: int, y: int) -> List[List[Optional[int]]]:
    """
    Ajoute la valeur 2 ou 4 à la position donnée dans la grille.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu actuelle.
        x (int): La position x où la nouvelle valeur sera ajoutée.
        y (int): La position y où la nouvelle valeur sera ajoutée.
        
    Returns:
        List[List[Optional[int]]]: La grille de jeu mise à jour avec le nouveau nombre ajouté.
    """
    # Choisir 2 (90% de chance) ou 4 (10% de chance)
    new_tile_value = 2 if random.random() < 0.9 else 4
    game_grid[x][y] = new_tile_value
    
    return game_grid
    


def add_new_tile(game_grid: List[List[Optional[int]]]) -> None:
    """
    Ajoute une nouvelle tuile de valeur 2 ou 4 à une position vide aléatoire de la grille.
    La valeur 2 est choisie avec une probabilité de 90%, sinon la valeur est 4.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu sous forme de liste de listes.
    
    Returns:
        None: La fonction modifie directement la grille sans retourner de valeur.
    """
    # Récupère les positions vides dans la grille
    empty_tiles = [(i, j) for i in range(len(game_grid)) for j in range(len(game_grid[i])) if game_grid[i][j] is None]
    
    # Si aucune position vide n'est disponible, termine la fonction
    if not empty_tiles:
        return

    # Choisit aléatoirement une position vide et y ajoute une tuile avec une valeur de 2 (90%) ou de 4 (10%)
    x, y = random.choice(empty_tiles)
    game_grid[x][y] = 2 if random.random() < 0.9 else 4


def get_value_new_tile() -> int:
    """
    Retourne la valeur d'une nouvelle tuile pour le jeu, soit 2 avec une probabilité de 90%, soit 4 avec une probabilité de 10%.
    
    Returns:
        int: La valeur de la tuile, soit 2 ou 4.
    """
    # Utilise une probabilité de 0.9 pour renvoyer 2, sinon renvoie 4
    return 2 if random.random() < 0.9 else 4


def get_all_tiles(game_grid: List[List[Optional[int]]]) -> List[List[int]]:
    """
    Retourne une copie de la grille contenant les valeurs de chaque tuile, où les cases vides (None)
    sont remplacées par 0.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu actuelle avec des tuiles.
        
    Returns:
        List[List[int]]: Une copie de la grille avec les cases vides remplacées par 0.
    """
    # Crée une copie de la grille en remplaçant None par 0 pour chaque cellule
    return [[cell if cell is not None else 0 for cell in row] for row in game_grid]