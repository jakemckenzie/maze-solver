class MazeSolver:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def solve(self, maze):
        pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )

class Cell:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = None

    def set_window(self, window):
        self._win = window

    def draw(self):
        if self._win:
            if self.has_left_wall:
                self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="black", width=2)
            if self.has_right_wall:
                self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="black", width=2)
            if self.has_top_wall:
                self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="black", width=2)
            if self.has_bottom_wall:
                self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="black", width=2)
