def read_player_command():
    """
    Fonction pour lire et valider la commande du joueur.
    La commande doit être l'une des directions suivantes : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    
    Returns:
        str: La commande validée par le joueur.
    """
    # Liste des directions possibles
    directions = ["g", "d", "h", "b"]
    
    # Demande de la commande au joueur
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)): ")
    
    # Vérification que la commande est valide
    while move not in directions:
        print("La commande saisie n'est pas valide.")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)): ")
    
    return move


def read_size_grid():
    """
    Fonction pour lire et valider la taille de la grille.
    La taille doit être un entier valide.

    Returns:
        int: La taille de la grille saisie par l'utilisateur.
    """
    # Demande de la taille de la grille
    size = input("Entrez la taille : ")
    
    # Vérification que la taille est un entier valide
    while not size.isdigit():
        print("La taille saisie n'est pas valide.")
        size = input("Entrez la taille : ")
    
    return int(size)  # Conversion de la taille en entier


def read_theme_grid():
    """
    Fonction pour lire le thème souhaité pour la grille.
    Le thème doit être un entier (0, 1 ou 2).

    Returns:
        str: Le thème choisi par l'utilisateur.
    """
    # Demande du thème souhaité
    theme = input("Entrez le thème souhaité :(0,1,2): ")
    
    # Retourner le thème saisi
    return theme
