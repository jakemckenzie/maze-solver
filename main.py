import tkinter as tk
from controller import Controller
from model import Line, Point
from view import Window

def main():
    root = tk.Tk()
    window = Window(root, 800, 600)
    controller = Controller(window)

    point1 = Point(69, 69)
    point2 = Point(420, 420)
    point3 = Point(420, 69)
    point4 = Point(69, 420)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point1)

    controller.draw_line(line1, "Red")
    controller.draw_line(line2, "Blue")
    controller.draw_line(line3, "Green")
    controller.draw_line(line4, "black")

    window.wait_for_close()

if __name__ == "__main__":
    main()
