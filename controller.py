from view import Window


class Controller:
    def __init__(self, root, width=800, height=600):
        self.window = Window(root, width, height)
        self.cells = []

    def run(self):
        while True:
            self.window.update()

    def draw_cell(self, cell):
        cell.set_window(self.window)
        cell.draw()