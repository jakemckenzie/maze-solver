import tkinter as tk

class Window:
    def __init__(self, root, width, height):
        self.root = root
        self.root.title("Maze Solver")
        self.root.geometry(f"{width}x{height}")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def update(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_lines(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def create_line(self, *args, **kwargs):
        self.canvas.create_line(*args, **kwargs)
