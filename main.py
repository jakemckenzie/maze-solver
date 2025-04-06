import tkinter as tk
from controller import Controller
from model import Maze
from constants import *
import sys

sys.setrecursionlimit(72*97)

def main():

    root = tk.Tk()
    controller = Controller(root, width=800, height=600)

    maze = Maze(
        x1=16,
        y1=16,
        num_rows=(2 * ROW_SIZE + 7),
        num_cols=(2 * COL_SIZE + 16),
        cell_size_x=8,
        cell_size_y=8,
        win=controller.window
    )

    maze._cells[0][0].has_top_wall = False
    maze._cells[COL_SIZE - 1][ROW_SIZE - 1].has_bottom_wall = False
    controller.draw_cell(maze._cells[0][0])
    controller.draw_cell(maze._cells[COL_SIZE - 1][ROW_SIZE - 1])

    maze.solve_min_cut()

    root.protocol("WM_DELETE_WINDOW", root.quit)
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting...")
        root.quit()

if __name__ == "__main__":
    main()