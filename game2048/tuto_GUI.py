from tkinter import *
from tkmacosx import Button

# Création de la fenêtre principale, racine de l'interface utilisateur
window = Tk()

# Création d'un label (une ligne de texte) affichant "Hello World !"
# Le label est associé à la fenêtre créée précédemment
label_field = Label(window, text="Hello World !")

# Affichage du label dans la fenêtre
label_field.pack()

# Lancement de la boucle principale Tkinter, se termine lorsque la fenêtre est fermée
window.mainloop()

import tkinter as tk

def write_text():
    """
    Fonction appelée lors du clic sur le bouton "Hello".
    Affiche un message dans la console.
    """
    print("Hello CentraleSupelec")

# Création de la fenêtre principale
root = tk.Tk()

# Création d'un conteneur (frame) pour organiser les widgets
frame = tk.Frame(root)
frame.pack()

# Bouton pour quitter l'application
button = tk.Button(
    frame,
    text="QUIT",                # Texte du bouton
    activebackground="blue",    # Couleur de fond lorsqu'il est actif
    fg="red",                   # Couleur du texte
    command=quit                # Action déclenchée lors du clic
)
button.pack(side=tk.LEFT)       # Placement du bouton à gauche dans le conteneur

# Bouton affichant "Hello" et déclenchant une action
slogan = tk.Button(
    frame,
    fg="blue",                  # Couleur du texte
    text="Hello",               # Texte du bouton
    command=write_text          # Action déclenchée lors du clic
)
slogan.pack(side=tk.TOP)        # Placement du bouton en haut dans le conteneur

# Lancement de la boucle principale Tkinter
root.mainloop()
