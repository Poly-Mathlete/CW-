
import random
from typing import List, Tuple, Optional


def create_grid(n = 4) -> List[List[Optional[int]]]:
    """
    Crée une grille de jeu (n x n) vide pour le jeu 2048.
    Args : 
        n (int) : la taille de la grille par défaut 4 . 
    Returns:
        List[List[Optional[int]]]: Une liste de listes représentant la grille, initialisée avec des valeurs None.
    """
    return [[None for _ in range(n)] for _ in range(n)]


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

def get_empty_tiles_positions(game_grid: List[List[Optional[int]]]) -> List[Tuple[int, int]]:
    """
    Retourne une liste des positions des cases vides (représentées par 0 ou ' ') dans la grille.

    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu.

    Returns:
        List[Tuple[int, int]]: Une liste de tuples représentant les positions (x, y) des cases vides.
    """
    empty_positions = []
    
    for i in range(len(game_grid)):
        for j in range(len(game_grid[i])):
            if game_grid[i][j] == 0 or game_grid[i][j] == ' ':
                empty_positions.append((i, j))
    
    return empty_positions

def grid_get_value(game_grid: List[List[Optional[int]]], x: int, y: int) -> Optional[int]:
    """
    Retourne la valeur à la position (x, y) dans la grille de jeu.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu.
        x (int): L'index de la ligne.
        y (int): L'index de la colonne.
    
    Returns:
        Optional[int]: La valeur de la case à la position (x, y).
    """
    return get_all_tiles(game_grid)[x][y]

def get_new_postion(game_grid: List[List[Optional[int]]]) -> List[List[int]]:
    """
      Retourne aléatoirement une position vide de la grille.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu.
    
    Returns:
        tuple[int, int]: Un tuple représentant les coordonnées (x, y) d'une position vide.
    """
    return random.choice(get_empty_tiles_positions(game_grid))

def init_game(n : int ) -> List[List[Optional[int]]]:
    """
    Débute le jeux en créant  , la grille et la tuile .

    Args:
        
        n (int): La taille de la grille . 

    Returns:
        List[List[Optional[int]]]: Une liste de listes représentant la grille.

    """
    get_all_tiles(add_new_tile(create_grid(n)))