import random
import time

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
    def __init__(self, x1, y1, x2, y2, win=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False

    def set_window(self, window):
        self._win = window

    def draw(self):
        if self._win:

            background_color = "#d9d9d9"

            if self.has_left_wall:
                self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill="black")
            else:
                self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill=background_color)

            if self.has_right_wall:
                self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill="black")
            else:
                self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill=background_color)

            if self.has_top_wall:
                self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill="black")
            else:
                self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill=background_color)

            if self.has_bottom_wall:
                self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill="black")
            else:
                self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill=background_color)

    def draw_move(self, to_cell, undo=False):
        if self._win:
            x1_center = (self.x1 + self.x2) / 2
            y1_center = (self.y1 + self.y2) / 2
            x2_center = (to_cell.x1 + to_cell.x2) / 2
            y2_center = (to_cell.y1 + to_cell.y2) / 2
            line_color = "gray" if undo else "red"
            self._win.create_line(x1_center, y1_center, x2_center, y2_center, fill=line_color, width=2)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited() 
        

    def _break_walls_r(self, i, j):
        current_cell = self._cells[j][i]
        current_cell.visited = True

        while True:
            directions = []

            if j > 0 and not self._cells[j - 1][i].visited:
                directions.append(('left', j - 1, i))

            if j < self.num_cols - 1 and not self._cells[j + 1][i].visited:
                directions.append(('right', j + 1, i))

            if i > 0 and not self._cells[j][i - 1].visited:
                directions.append(('top', j, i - 1))

            if i < self.num_rows - 1 and not self._cells[j][i + 1].visited:
                directions.append(('bottom', j, i + 1))
                
            if not directions:
                self._draw_cell(i, j)
                return

            direction, next_j, next_i = random.choice(directions)

            if direction == 'left':
                current_cell.has_left_wall = False
                self._cells[next_j][next_i].has_right_wall = False
            elif direction == 'right':
                current_cell.has_right_wall = False
                self._cells[next_j][next_i].has_left_wall = False
            elif direction == 'top':
                current_cell.has_top_wall = False
                self._cells[next_j][next_i].has_bottom_wall = False
            elif direction == 'bottom':
                current_cell.has_bottom_wall = False
                self._cells[next_j][next_i].has_top_wall = False

            self._break_walls_r(next_i, next_j)

    def _create_cells(self):
        for j in range(self.num_cols):
            column = []
            for i in range(self.num_rows):
                cell_x1 = self.x1 + j * self.cell_size_x
                cell_y1 = self.y1 + i * self.cell_size_y
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y
                cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2, self.win)
                column.append(cell)
            self._cells.append(column)

        if self.win is not None:
            for j in range(self.num_cols):
                for i in range(self.num_rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[j][i]
        cell.draw()
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.update()
            time.sleep(0.001)
    
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)
    
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[j][i]
        current_cell.visited = True

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        directions = [
            ('left', 0, -1, 'has_left_wall'),
            ('right', 0, 1, 'has_right_wall'),
            ('up', -1, 0, 'has_top_wall'),
            ('down', 1, 0, 'has_bottom_wall')
        ]
        
        for _, di, dj, wall_attr in directions:
            adj_i = i + di
            adj_j = j + dj

            if 0 <= adj_i < self.num_rows and 0 <= adj_j < self.num_cols:
                adj_cell = self._cells[adj_j][adj_i]

                if not adj_cell.visited and not getattr(current_cell, wall_attr):
                    current_cell.draw_move(adj_cell)
                    if self._solve_r(adj_i, adj_j):
                        return True
                    else:
                        current_cell.draw_move(adj_cell, undo=True)
        
        return False
    
    def solve(self):
        return self._solve_r(0, 0)
    