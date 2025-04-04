import tkinter as tk
from controller import Controller
from model import Maze

def main():
    root = tk.Tk()
    controller = Controller(root, width=800, height=600)

    maze = Maze(
        x1=16,
        y1=16,
        num_rows=32,
        num_cols=40,
        cell_size_x=16,
        cell_size_y=16,
        win=controller.window
    )


    cell1 = maze._cells[0][0]
    cell2 = maze._cells[1][0]
    cell3 = maze._cells[1][1]
    cell4 = maze._cells[0][1]

    cell2.has_top_wall = False
    cell3.has_bottom_wall = False
    cell4.has_left_wall = False
    cell4.has_right_wall = False

    controller.draw_cell(cell2)
    controller.draw_cell(cell3)
    controller.draw_cell(cell4)

    root.protocol("WM_DELETE_WINDOW", root.quit)
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting...")
        root.quit()

if __name__ == "__main__":
    main()