from view import Window
from model import MazeSolver

class Controller:
    def __init__(self, root):
        self.window = Window(root)
        self.maze_solver = MazeSolver()

    def run(self):
        while True:
            self.window.update()