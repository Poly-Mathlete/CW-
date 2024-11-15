import tkinter as tk
import game2048.colors as c
from game2048.grid_2048 import *
import keyboard


class Game(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self)
        self.root = root
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(self, bg=c.GRID_COLOR, bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.start_game()
        self.bind_keys()
        self.mainloop()

    def make_GUI(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(self.main_grid, bg=c.EMPTY_CELL_COLOR, width=150, height=150)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(score_frame, text="Score", font=c.SCORE_LABEL_FONT).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)

    def start_game(self):
        # Initialise la grille du jeu
        self.grid_data = init_game(n=4)
        self.update_GUI()

    def bind_keys(self):
        # Associer les touches directionnelles
        self.root.bind("<Up>", lambda event: self.move("up"))
        self.root.bind("<Down>", lambda event: self.move("down"))
        self.root.bind("<Left>", lambda event: self.move("left"))
        self.root.bind("<Right>", lambda event: self.move("right"))

    def move(self, direction):
        # Effectuer un déplacement dans la direction spécifiée
        self.grid_data = move_grid(self.grid_data, direction)
        self.grid_data = grid_add_new_tile(self.grid_data)
        self.update_GUI()

        # Vérifier si le jeu est terminé
        if is_game_over(self.grid_data):
            self.game_over()

    def game_over(self):
        game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
        game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(game_over_frame, text="Game Over", font=c.GAME_OVER_FONT, fg=c.GAME_OVER_FONT_COLOR).pack()

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                val = self.grid_data[i][j]
                if val == 0:
                    self.cells[i][j]["frame"].config(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].config(bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].config(bg=c.CELL_COLORS.get(val, "#f0f0f0"))
                    self.cells[i][j]["number"].config(
                        bg=c.CELL_COLORS.get(val, "#f0f0f0"),
                        fg="#776e65" if val <= 4 else "#f9f6f2",
                        font=c.CELL_NUMBER_FONTS.get(val, ("Helvetica", 30, "bold")),
                        text=str(val)
                    )


# Lancer le jeu
root = tk.Tk()
game = Game(root)
