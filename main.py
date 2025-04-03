import tkinter as tk
from controller import Controller
from model import Cell

def main():
    root = tk.Tk()
    controller = Controller(root, width=800, height=600)

    cell1 = Cell(50, 50, 150, 150)
    cell2 = Cell(200, 50, 300, 150)
    cell3 = Cell(50, 200, 150, 300)
    cell4 = Cell(200, 200, 300, 300)

    cell2.has_top_wall = False
    cell3.has_bottom_wall = False
    cell4.has_left_wall = False
    cell4.has_right_wall = False

    controller.draw_cell(cell1)
    controller.draw_cell(cell2)
    controller.draw_cell(cell3)
    controller.draw_cell(cell4)

    controller.run()

if __name__ == "__main__":
    main()

