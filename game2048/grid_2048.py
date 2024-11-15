import tkinter as tk
import random as rd

# Importer les fonctions du jeu depuis votre module.
# Par exemple, create_grid, grid_add_new_tile, move_grid, etc.

THEMES = {
    "0": {"name": "Default", 0: 0, 2: 2, 4: 4, 8: 8, 16: 16, 32: 32, 64: 64, 128: 128, 256: 256, 512: 512, 1024: 1024, 2048: 2048, 4096: 4096, 8192: 8192},
    "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
    "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}
}

def create_grid(n=4):
    return [[0 for _ in range(n)] for _ in range(n)]

def grid_add_new_tile(game_grid):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if game_grid[i][j] == 0]
    if empty_tiles:
        i, j = rd.choice(empty_tiles)
        game_grid[i][j] = rd.choice([2, 4])
    return game_grid

def move_grid(grid, direction):
    if direction == 'left':
        return [move_row_left(row) for row in grid]
    elif direction == 'right':
        return [move_row_right(row) for row in grid]
    elif direction == 'up':
        return transpose_grid([move_row_left(row) for row in transpose_grid(grid)])
    elif direction == 'down':
        return transpose_grid([move_row_right(row) for row in transpose_grid(grid)])
    return grid

def transpose_grid(grid):
    return [list(row) for row in zip(*grid)]

def move_row_left(row):
    new_row = [i for i in row if i != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0]
    return new_row + [0] * (len(row) - len(new_row))

def move_row_right(row):
    return move_row_left(row[::-1])[::-1]

def grid_to_string(grid):
    return "\n".join(" ".join(str(cell) if cell != 0 else '.' for cell in row) for row in grid)

def is_game_over(grid):
    return all(cell != 0 for row in grid for cell in row)

class Game2048(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_size = 4
        self.grid = create_grid(self.grid_size)
        self.grid = grid_add_new_tile(self.grid)  # Adding first tile
        self.create_gui()
        self.update_gui()
        self.bind_keys()
        self.mainloop()

    def create_gui(self):
        self.main_grid = tk.Frame(self, bg="lightgray", bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100, 0), padx=10)

        self.cells = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                cell_frame = tk.Frame(self.main_grid, bg="white", width=150, height=150)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg="white", text="", font=("Helvetica", 24, "bold"))
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

    def bind_keys(self):
        self.master.bind("<Left>", lambda event: self.move("left"))
        self.master.bind("<Right>", lambda event: self.move("right"))
        self.master.bind("<Up>", lambda event: self.move("up"))
        self.master.bind("<Down>", lambda event: self.move("down"))

    def move(self, direction):
        self.grid = move_grid(self.grid, direction)
        self.grid = grid_add_new_tile(self.grid)
        self.update_gui()
        if is_game_over(self.grid):
            self.show_game_over()

    def update_gui(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                if value == 0:
                    self.cells[i][j]["frame"].config(bg="lightgray")
                    self.cells[i][j]["number"].config(text="")
                else:
                    self.cells[i][j]["frame"].config(bg="orange" if value == 2 else "yellow")
                    self.cells[i][j]["number"].config(text=str(value))

    def show_game_over(self):
        game_over_label = tk.Label(self, text="Game Over", font=("Helvetica", 30, "bold"), fg="red")
        game_over_label.place(relx=0.5, rely=0.4, anchor="center")

# Lancer le jeu
root = tk.Tk()
root.title("2048 Game")
root.mainloop()
game = Game2048(root)
