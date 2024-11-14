import numpy 

def read_player_command() -> str :
    """
    Cette fonction va retourner la commande de l'utilisateur .
    
    """
    Directions = ["g","d","h","b"]
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in Directions :
        print("La commande saisie n'est pas valide.")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")

    return move


def read_size_grid() -> int:
    """
    Cette fonction va retourner le choix de taille fait par l'utilisateur.
    Elle vérifie que l'entrée est un entier valide.
    """
    while True:
        try:
            size = int(input("Entrez la taille :"))
            return size  # Si la conversion réussit, retourne la taille
        except ValueError:
            print("La taille saisie n'est pas valide. Veuillez entrer un nombre entier.")


def read_theme_grid() -> str:
    """
    Fonction qui demande à l'utilisateur de choisir un thème parmi les options disponibles.
    La fonction valide l'entrée pour s'assurer que le thème est valide.
    
    Returns:
        str: Le thème validé par l'utilisateur.
    """
    # Demander à l'utilisateur de saisir un thème
    theme = input("Entrez le thème souhaité (0, 1, 2) : ")
    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

    # Vérifier si le thème est valide
    while theme not in THEMES:
        print("Thème invalide. Veuillez entrer un numéro valide parmi 0, 1, 2.")
        theme = input("Entrez le thème souhaité (0, 1, 2) : ")
    
    return theme

