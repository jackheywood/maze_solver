from models.window import Window
from models.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 55, 7, 10, 70, win)
    maze.solve()

    win.wait_for_close()


main()
