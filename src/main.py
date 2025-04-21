from models.window import Window
from models.maze import Maze


def main():
    width = 1200
    height = 800
    padding = 100
    size = 50
    rows = (height - (2 * padding)) // size
    cols = (width - (2 * padding)) // size

    window = Window(width, height)

    maze = Maze(padding, padding, rows, cols, size, window)
    maze.solve()

    window.wait_for_close()


main()
