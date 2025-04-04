import unittest
from model import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_small(self):
        num_cols = 1
        num_rows = 1
        m2 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 15
        m3 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)

    def test_reset_cells_visited(self):
        maze = Maze(x1=0, y1=0, num_rows=3, num_cols=3, cell_size_x=10, cell_size_y=10)

        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        maze._cells[2][2].visited = True

        maze._reset_cells_visited()

        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()