import tkinter as tk
from controller import Controller

def main():
    root = tk.Tk()
    app = Controller(root)
    app.run()

if __name__ == "__main__":
    main()
