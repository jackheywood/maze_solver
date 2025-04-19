import time
from models.cell import Cell


class Maze:
    def __init__(self, window, x, y, rows, cols, cell_size):
        self.__window = window
        self.__x = x
        self.__y = y
        self.__rows = rows
        self.__cols = cols
        self.__cell_size = cell_size
        self.__create_cells()
        self.__draw_cells()

    def __create_cells(self):
        self.__cells = []
        for col in range(self.__cols):
            col_cells = []
            for row in range(self.__rows):
                col_cells.append(Cell(
                    self.__window,
                    self.__x + col * self.__cell_size,
                    self.__y + row * self.__cell_size,
                    self.__cell_size
                ))
            self.__cells.append(col_cells)

    def __draw_cells(self):
        for col in self.__cells:
            for cell in col:
                cell.draw()
                self.__animate()

    def __animate(self):
        self.__window.redraw()
        time.sleep(0.05)
