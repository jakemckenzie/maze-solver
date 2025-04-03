class Controller:
    def __init__(self, window):
        self.window = window
        #self.maze_solver = MazeSolver()

    def run(self):
        while True:
            self.window.update()
    
    def draw_line(self, line, fill_color):
        line.draw(self.window.canvas, fill_color)
