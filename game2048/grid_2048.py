
import random
from typing import List, Tuple, Optional


def create_grid(n = 4) -> List[List[Optional[int]]]:
    """
    Crée une grille de jeu (n x n) vide pour le jeu 2048.
    Args : 
        n (int) : la taille de la grille par défaut 4 . 
    Returns:
        List[List[Optional[int]]]: Une liste de listes représentant la grille, initialisée avec des valeurs ''.
    """
    return [[' ' for _ in range(n)] for _ in range(n)]

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



def grid_add_new_tile(game_grid: List[List[Optional[int]]]) -> None :
    """
    Ajoute une nouvelle tuile de valeur 2 ou 4 à une position vide aléatoire de la grille.
    La valeur 2 est choisie avec une probabilité de 90%, sinon la valeur est 4.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu sous forme de liste de listes.
    
    Returns:
        None : La fonction modifie directement la grille et retourne la grille .
    """
    # Récupère les positions vides dans la grille
    empty_tiles = [(i, j) for i in range(len(game_grid)) for j in range(len(game_grid[i])) if game_grid[i][j] == ' ' or game_grid[i][j] == 0]
    
    # Si aucune position vide n'est disponible, retourne la grille
    if not empty_tiles:
        return game_grid

    # Choisit aléatoirement une position vide et y ajoute une tuile avec une valeur de 2 (90%) ou de 4 (10%)
    x, y = random.choice(empty_tiles)
    game_grid[x][y] = 2 if random.random() < 0.9 else 4
    return game_grid


def get_value_new_tile() -> int:
    """
    Retourne la valeur d'une nouvelle tuile pour le jeu, soit 2 avec une probabilité de 90%, soit 4 avec une probabilité de 10%.
    
    Returns:
        int: La valeur de la tuile, soit 2 ou 4.
    """
    # Utilise une probabilité de 0.9 pour renvoyer 2, sinon renvoie 4
    return 2 if random.random() < 0.9 else 4



def get_all_tiles(game_grid: List[List[Optional[int]]]) -> List[int]:
    """
    Retourne une copie de la grille contenant les valeurs de chaque tuile, où les cases vides (' ')
    sont remplacées par 0, et la liste est aplatie en une seule dimension.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu actuelle avec des tuiles.
        
    Returns:
        List[int]: Une copie aplatie de la grille avec les cases vides remplacées par 0.
    """
    if  game_grid is None :
        game_grid = create_grid()
    # Remplace ' ' par 0 et aplatie la grille en une seule liste
    return [cellule if cellule != ' ' else 0 for row in game_grid for cellule in row]


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
    if game_grid is None :
        game_grid = create_grid()
    return game_grid[x][y] if game_grid[x][y] != ' ' else 0

def get_new_position(game_grid: List[List[Optional[int]]]) -> List[List[int]]:
    """
      Retourne aléatoirement une position vide de la grille.
    
    Args:
        game_grid (List[List[Optional[int]]]): La grille de jeu.
    
    Returns:
        tuple[int, int]: Un tuple représentant les coordonnées (x, y) d'une position vide.
    """
    return random.choice(get_empty_tiles_positions(game_grid))

def init_game(n: int) -> List[List[Optional[int]]]:
    """
    Starts the game by creating the grid and adding an initial tile.

    Args:
        n (int): The size of the grid.

    Returns:
        List[List[Optional[int]]]: A list of lists representing the grid with an initial tile.
    """
    # Create an empty grid
    grid = create_grid(n)
    
    # Ajout de la première tuile
    grid_add_new_tile(grid) 

    # Ajout de la deuxième tuile 
    grid_add_new_tile(grid) 

    
    return grid



def grid_to_string_with_size(grid:List[List[Optional[int]]], n : int = 4 ) -> str:
    """
    Retourne une chaîne représentant la grille avec une taille de cellule ajustée et 
    des séparateurs pour chaque ligne et chaque colonne.
    
    Args:
        grid (List[List[Optional[int]]]): La grille de jeu à formater.
        n (int, optional): La taille de la grille (par défaut 4).

    Returns:
        str: La grille formatée en chaîne de caractères avec des séparateurs et des cases.
    """
    # Définir le séparateur de ligne (les signes ===)
    a = ' ==='  # Début de la première ligne
    # Ajouter un séparateur de ligne pour chaque colonne sauf la dernière
    for k in range(n-1):
        a += ' ==='  # Ajouter un séparateur supplémentaire pour chaque colonne
    a += '\n'  # Ajouter un saut de ligne à la fin de la première ligne

    # Parcourir chaque ligne de la grille
    for i in range(n):
        # Parcourir chaque élément de la ligne
        for j in range(n):
            # Ajouter le séparateur de colonne et la valeur de chaque cellule
            a += '| ' + str(grid[i][j]) + ' '  # Convertir la valeur en chaîne et l'ajouter
            m = long_value(grid)  # Longueur de la valeur maximale
            # Ajouter des espaces si la cellule actuelle est plus petite que la taille maximale
            if k != m:
                for g in range(m-k):  # Calculer l'espace manquant
                    a += ' '  # Ajouter les espaces nécessaires
        a += '|\n'  # Fin de la ligne de la grille (après les valeurs des cellules)

        # Ajouter les séparateurs de ligne après chaque ligne (sauf la dernière)
        for l in range(n):
            a += ' ==='  # Séparateur de ligne
        a += '\n'  # Nouvelle ligne après la ligne de séparation

    # Ajouter des espaces à la fin (si nécessaire) et retourner le résultat
    a += '   '
    return a  # Retourner la chaîne construite représentant la grille


def long_value(grid):
    L = get_all_tiles(grid)
    S = [len(str(L[i])) for i in range(len(grid))]
    return max(S)

def long_value_with_theme( grid:List[List[Optional[int]]] , d: dict ) -> int :
    """
    Calcule la longueur maximale des valeurs dans la grille de jeu après avoir aplati la grille.
    
    Args:
        grid (List[List[Optional[int]]]): La grille de jeu (listes de listes contenant des entiers ou None).
        
    Returns:
        int: La longueur maximale des valeurs dans la grille.
    """
    L = get_all_tiles(grid)  # Aplatir la grille et remplacer les cases vides par 0
    S = [len(d[L[i]]) for i in range(len(L))]  # Calculer la longueur de chaque valeur de la liste aplatie
    return max(S)  # Retourner la longueur maximale

def grid_to_string_with_size_and_theme(grid: List[List[Optional[int]]], d: dict, n: int = 4) -> str:
    """
    Retourne une représentation sous forme de chaîne de la grille de jeu avec un thème et un ajustement de taille des cellules.
    
    Args:
        grid (List[List[Optional[int]]]): La grille de jeu.
        d (dict): Un dictionnaire où les clés sont les valeurs de la grille et les valeurs sont des représentations sous forme de chaînes (thème).
        n (int, optional): La taille de la grille, par défaut 4.
    
    Returns:
        str: La chaîne représentant la grille avec le thème appliqué et les cellules de taille ajustée.
    """
    n = len(grid)  # La taille de la grille (n x n)
    
    # Obtenir la longueur maximale d'une valeur dans la grille en fonction du thème
    m = long_value_with_theme(grid, d)
    
    # Initialisation de la chaîne avec les séparateurs de ligne
    a = '============'  # 12 signes égal pour les séparateurs de ligne
    for k in range(n-1):
        a += '==='  # Ajouter des séparateurs pour chaque colonne
    a += '\n'  # Ajouter un saut de ligne à la fin de la première ligne
    
    # Parcourir chaque ligne de la grille
    for i in range(n):
        # Parcourir chaque colonne de la ligne
        for j in range(n):
            # Ajouter le thème associé à la valeur de la cellule
            a += '| ' + d[grid[i][j]]  # Représentation thématique de la cellule
            k = len(d[grid[i][j]])  # Longueur du texte de la cellule
            # Ajouter des espaces pour uniformiser la taille des cellules
            if k != m:
                for g in range(m - k):  # Calculer l'espace manquant
                    a += ' '  # Ajouter l'espace nécessaire
        a += ' |\n'  # Fin de la ligne et ajout d'un séparateur

        # Ajouter les séparateurs de ligne après chaque ligne (sauf la dernière)
        for l in range(n):
            a += '==='  # Séparateur de ligne
        a += '\n'  # Nouvelle ligne après les séparateurs

    # Retourner la chaîne sans le dernier caractère de séparation supplémentaire
    return a[:-1]


''' ~ MAINTENANT ON VA CODER LES MOUVEMENTS ~ '''

def move_row_left(row: list) -> list:
    """
    Cette fonction simule le mouvement d'une ligne vers la gauche dans un jeu comme 2048.
    Les éléments non nuls se déplacent vers la gauche et les éléments identiques se fusionnent 
    (se multiplient par 2) si cela n'a pas déjà été fait.

    Args:
        row (list): Une ligne du jeu représentée par une liste d'entiers (0 pour une case vide).

    Returns:
        list: La nouvelle ligne après le mouvement vers la gauche.
    """
    # Filtrer les éléments non nuls
    non_nul = [i for i in row if i != 0]
    
    # Longueur de la ligne d'origine
    n = len(row)
    
    # Nombre d'éléments non nuls
    m = len(non_nul)
    
    # Liste pour suivre les éléments qui ont été fusionnés
    merged = [False] * len(non_nul)

    # Parcours des éléments non nuls pour effectuer les fusions
    for i in range(1, m):
        # Fusionner les éléments identiques et non fusionnés
        if non_nul[m - i] == non_nul[m - i - 1] and not merged[m - i] and not merged[m - i - 1]:
            # Doubler la valeur de l'élément précédent
            non_nul[m - i - 1] *= 2
            # Remettre la case fusionnée à 0
            non_nul[m - i] = 0
            # Marquer les éléments comme fusionnés
            merged[m - i] = True
            merged[m - i - 1] = True

    # Compléter la liste avec des zéros pour revenir à la taille d'origine
    L_to_left = non_nul.extend([0] * (n - len(non_nul)))

    return L_to_left


