def read_player_command():
    Directions = ["g","d","h","b"]
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in Directions :
        print("La commande saisie n'est pas valide.")
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def read_size_grid():
    size = input("Entrez la taille :")
    while type(size) != int:
        print("La taille saisie n'est pas valide.")
        size = input("Entrez la taille :")        
    return size
def read_theme_grid():
    theme = input("Entrez le thème souhaité :(0,1,2)")
    return theme