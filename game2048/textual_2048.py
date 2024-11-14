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


