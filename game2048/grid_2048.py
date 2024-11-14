
import random
import numpy as np
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

def grid_to_string_with_size_and_theme(grid:List[List[Optional[int]]], d: dict , n : int = 4):
    """
    Fonction qui génère une chaîne de caractères représentant une grille avec 
    des valeurs formatées selon un thème donné.

    Args:
        grid (list): La grille à afficher.
        d (dict): Un dictionnaire qui mappe les valeurs de la grille à leurs représentations en texte.
        n (int): La taille de la grille (par défaut 4).

    Returns:
        str: Une chaîne de caractères formatée représentant la grille.
    """
    # Calcul du nombre de caractères à utiliser pour les cases
    n = len(grid)  # On redéfinit n à la taille de la grille
    m = long_value_with_theme(grid, d)  # Longueur maximale de la valeur dans la grille en fonction du thème

    # Initialisation de la chaîne avec les bords de la grille
    a = '===='
    for k in range(n - 1):
        a += '==='  # Ajout des bords pour chaque colonne
    
    a += '\n'

    # Parcours des lignes de la grille
    for i in range(n):
        for j in range(n):
            # Ajout de la valeur de la case courante en fonction du thème
            a += '|' + d[grid[i][j]]
            k = len(d[grid[i][j]])  # Longueur de la représentation en texte de la valeur
            if k != m:  # Si la longueur est inférieure à la longueur maximale
                for g in range(m - k):  # Ajouter des espaces pour égaliser la longueur
                    a += ' '

        a += '|\n'  # Fin de la ligne

        # Ajout des bords horizontaux pour chaque ligne
        a += '='
        for l in range(n):
            a += '==='  # Ajout des bords pour chaque colonne

        a += '\n'

    # Retourner la chaîne sans le dernier retour à la ligne supplémentaire
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
    
    # Liste pour suivre les éléments qui ont été fusionnés
    merged = [False] * len(non_nul)

    # Parcours des éléments non nuls pour effectuer les fusions
    i = 0
    while i < len(non_nul) - 1:
        # Si les éléments sont identiques et non fusionnés
        if non_nul[i] == non_nul[i + 1] and not merged[i] and not merged[i + 1]:
            # Fusionner les éléments
            non_nul[i] *= 2
            non_nul[i + 1] = 0
            merged[i] = True  # Marquer comme fusionné
            merged[i + 1] = True
            i += 1  # Passer à l'élément suivant après la fusion
        i += 1

    # Filtrer à nouveau pour enlever les zéros (en cas de fusion)
    non_nul = [i for i in non_nul if i != 0]

    # Compléter la liste avec des zéros pour revenir à la taille d'origine
    L_to_left = non_nul + [0] * (n - len(non_nul))

    return L_to_left

def move_row_right(row: list) -> list:
    """
    Cette fonction simule le mouvement d'une ligne vers la droite dans un jeu comme 2048.
    Les éléments non nuls se déplacent vers la droite et les éléments identiques se fusionnent 
    (se multiplient par 2) si cela n'a pas déjà été fait.

    Args:
        row (list): Une ligne du jeu représentée par une liste d'entiers (0 pour une case vide).

    Returns:
        list: La nouvelle ligne après le mouvement vers la droite.
    """
    # Filtrer les éléments non nuls
    non_nul = [i for i in row if i != 0]
    
    # Longueur de la ligne d'origine
    n = len(row)
    
    # Liste pour suivre les éléments qui ont été fusionnés
    merged = [False] * len(non_nul)

    # Parcours des éléments non nuls de droite à gauche pour effectuer les fusions
    i = len(non_nul) - 1
    while i > 0:
        # Si les éléments sont identiques et non fusionnés
        if non_nul[i] == non_nul[i - 1] and not merged[i] and not merged[i - 1]:
            # Fusionner les éléments
            non_nul[i] *= 2
            non_nul[i - 1] = 0
            merged[i] = True  # Marquer comme fusionné
            merged[i - 1] = True
            i -= 1  # Passer à l'élément suivant après la fusion
        i -= 1

    # Filtrer à nouveau pour enlever les zéros (en cas de fusion)
    non_nul = [i for i in non_nul if i != 0]

    # Compléter la liste avec des zéros à gauche pour revenir à la taille d'origine
    L_to_right = [0] * (n - len(non_nul)) + non_nul

    return L_to_right


def move_grid(grid: List[List[Optional[int]]], direction: str) -> List[List[Optional[int]]]:
    """
    Simule le mouvement d'une grille dans une direction donnée ('l', 'r', 'u', 'd') pour un jeu de type 2048.
    
    Args:
        grid (List[List[Optional[int]]]): La grille du jeu représentée par une liste de listes d'entiers.
        direction (str): La direction du mouvement ('l' pour gauche, 'r' pour droite, 'u' pour haut, 'd' pour bas).

    Returns:
        List[List[Optional[int]]]: La grille après l'application du mouvement.
    """
    directions = {"l": "left", "r": "right", "u": "up", "d": "down"}
    
    if direction[0] not in directions:
        print("La direction saisie n'est pas valide. Veuillez entrer une direction parmi 'l', 'r', 'u' ou 'd'.")
        return grid

    if direction[0] == 'l':
        for j in range(len(grid)):
            grid[j] = move_row_left(grid[j]) 

    elif direction[0] == 'r':
        for j in range(len(grid)):
            grid[j] = move_row_right(grid[j]) 

    elif direction[0] == 'u':
        transposed_grid = np.array(grid).T.tolist()
        for j in range(len(transposed_grid)):
            transposed_grid[j] = move_row_left(transposed_grid[j])
        grid[:] = np.array(transposed_grid).T.tolist()

    elif direction[0] == 'd':
        transposed_grid = np.array(grid).T.tolist()
        for j in range(len(transposed_grid)):
            transposed_grid[j] = move_row_right(transposed_grid[j])
        grid[:] = np.array(transposed_grid).T.tolist()
    
    return grid

import numpy as np

def is_grid_full(grid) -> bool:
    """
    Vérifie si la grille est pleine en recherchant des cases vides (0 ou espace).
    
    Args:
        grid (List[List[Optional[int]]]): Grille de jeu 2D.

    Returns:
        bool: True si la grille est pleine, sinon False.
    """
    # Convertir la grille en un tableau NumPy pour les opérations vectorisées
    grid_np = np.array(grid)
    
    # Vérifier s'il y a des cases vides (0 ou ' ')
    return not np.any((grid_np == 0) | (grid_np == ' '))

