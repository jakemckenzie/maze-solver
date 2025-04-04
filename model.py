import time

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
                self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="black")
            if self.has_right_wall:
                self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="black")
            if self.has_top_wall:
                self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="black")
            if self.has_bottom_wall:
                self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="black")

    def draw_move(self, to_cell, undo=False):
        if self._win:
            x1_center = (self.x1 + self.x2) / 2
            y1_center = (self.y1 + self.y2) / 2
            x2_center = (to_cell.x1 + to_cell.x2) / 2
            y2_center = (to_cell.y1 + to_cell.y2) / 2
            line_color = "gray" if undo else "red"
            self._win.create_line(x1_center, y1_center, x2_center, y2_center, fill=line_color, width=2)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        
        for j in range(self.num_cols):
            column = []
            for i in range(self.num_rows):

                cell_x1 = self.x1 + j * self.cell_size_x
                cell_y1 = self.y1 + i * self.cell_size_y
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y

                cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2)
                cell.set_window(self.win)
                column.append(cell)
            self._cells.append(column)

        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[j][i]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.update()
        time.sleep(0.05)