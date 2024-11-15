import tkinter as tk
import random as rd
from game2048.colors import *
# Define game functions
def create_grid(n=4):
    """Create a 4x4 grid initialized with zeros."""
    return [[0 for _ in range(n)] for _ in range(n)]

def grid_add_new_tile(game_grid):
    """Add a new tile (2 or 4) to a random empty cell in the grid."""
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if game_grid[i][j] == 0]
    if empty_tiles:
        i, j = rd.choice(empty_tiles)
        game_grid[i][j] = rd.choice([2, 4])
    return game_grid

def transpose_grid(grid):
    """Transpose the grid (rows become columns and vice versa)."""
    return [list(row) for row in zip(*grid)]

def move_row_left(row):
    """Move and merge numbers to the left."""
    new_row = [i for i in row if i != 0]  # Remove all zeros
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0]  # Remove zeros after merging
    return new_row + [0] * (len(row) - len(new_row))

def move_row_right(row):
    """Move and merge numbers to the right."""
    return move_row_left(row[::-1])[::-1]

def move_grid(grid, direction):
    """Move the entire grid in the specified direction."""
    if direction == 'left':
        return [move_row_left(row) for row in grid]
    elif direction == 'right':
        return [move_row_right(row) for row in grid]
    elif direction == 'up':
        return transpose_grid([move_row_left(row) for row in transpose_grid(grid)])
    elif direction == 'down':
        return transpose_grid([move_row_right(row) for row in transpose_grid(grid)])
    return grid

def is_game_over(grid):
    """Check if no moves are left (either no zeros or no adjacent matching numbers)."""
    if any(0 in row for row in grid):
        return False
    for i in range(4):
        for j in range(4):
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True

class Game2048(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_size = 4
        self.grid = create_grid(self.grid_size)
        self.grid = grid_add_new_tile(self.grid)  # Adding the first tile
        self.grid = grid_add_new_tile(self.grid)  # Adding the second tile
        self.create_gui()
        self.update_gui()
        self.bind_keys()
        self.pack()

    def create_gui(self):
        """Set up the GUI for the game."""
        self.main_grid = tk.Frame(self, bg="gray", bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100, 0))

        self.cells = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                cell_frame = tk.Frame(self.main_grid, bg=GRID_COLOR, width=150, height=150)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=EMPTY_CELL_COLOR, text="", font=("Arial", 40, "bold"), width=4, height=2)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # Score display
        self.score = 0
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=30, anchor="center")
        tk.Label(score_frame, text="Score", font=("Helvetica", 20)).grid(row=0)
        self.score_label = tk.Label(score_frame, text=str(self.score), font=("Helvetica", 20))
        self.score_label.grid(row=1)

    def bind_keys(self):
        """Bind arrow keys to game controls."""
        self.master.bind("<Left>", lambda event: self.move("left"))
        self.master.bind("<Right>", lambda event: self.move("right"))
        self.master.bind("<Up>", lambda event: self.move("up"))
        self.master.bind("<Down>", lambda event: self.move("down"))

    def move(self, direction):
        """Handle grid movement and check game status."""
        new_grid = move_grid(self.grid, direction)
        if new_grid != self.grid:
            self.grid = grid_add_new_tile(new_grid)
            self.update_gui()
            if is_game_over(self.grid):
                self.show_game_over()

    def update_gui(self):
        """Update the GUI to reflect the current grid."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                if value == 0:
                    self.cells[i][j]["frame"].config(bg=EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    self.cells[i][j]["frame"].config(bg=self.get_color(value))
                    self.cells[i][j]["number"].config(text=str(value), bg=self.get_color(value), fg="black")
        self.score_label.config(text=str(self.calculate_score()))

    def get_color(self, value):
        """Return color based on the tile's value."""
        colors = {
            2: "#fcefe6",
            4: "#f2e8cb",
            8: "#f5b682",
            16: "#f29446",
            32: "#ff775c",
            64: "#e64c2e",
            128: "#ede291",
            256: "#fce130",
            512: "#ffdb4a",
            1024: "#f0b922",
            2048: "#fad74d",
        }
        return colors.get(value)

    def calculate_score(self):
        """Calculate the total score."""
        return sum(sum(row) for row in self.grid)

    def show_game_over(self):
        """Display 'Game Over' message."""
        game_over_label = tk.Label(self, text="Game Over", font=("Helvetica", 30, "bold"), fg="red")
        game_over_label.place(relx=0.5, rely=0.4, anchor="center")

# Run the game
root = tk.Tk()
root.title("2048 Game")
game = Game2048(root)
game.mainloop()
