from models.window import Window
from models.maze import Maze


def main():
    win = Window(800, 600)

    Maze(100, 100, 8, 12, 50, win)

    win.wait_for_close()


main()
