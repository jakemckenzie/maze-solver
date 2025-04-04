import tkinter as tk
from controller import Controller
from model import Maze

def main():
    root = tk.Tk()
    controller = Controller(root, width=800, height=600)

    maze = Maze(
        x1=50,
        y1=50,
        num_rows=4,
        num_cols=4,
        cell_size_x=50,
        cell_size_y=50,
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

    controller.draw_move(cell1, cell2)
    controller.draw_move(cell2, cell3)
    controller.draw_move(cell3, cell4)
    controller.draw_move(cell4, cell1, undo=True)

    root.protocol("WM_DELETE_WINDOW", root.quit)
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting...")
        root.quit()

if __name__ == "__main__":
    main()