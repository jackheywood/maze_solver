from models.window import Window
from models.maze import Maze


def main():
    win = Window(800, 600)

    Maze(50, 55, 7, 10, 70, win)

    win.wait_for_close()


main()
