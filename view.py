import tkinter as tk

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def update(self):
        self.root.update_idletasks()
        self.root.update()