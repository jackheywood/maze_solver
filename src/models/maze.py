import time
from models.cell import Cell


class Maze:
    def __init__(self, x, y, rows, cols, cell_size, window=None):
        self.__x = x
        self.__y = y
        self.__rows = rows
        self.__cols = cols
        self.__cell_size = cell_size
        self.__window = window
        self.__create_cells()
        self.__draw_cells()

    def __create_cells(self):
        self._cells = []
        for col in range(self.__cols):
            col_cells = []
            for row in range(self.__rows):
                col_cells.append(Cell(
                    self.__x + col * self.__cell_size,
                    self.__y + row * self.__cell_size,
                    self.__cell_size,
                    self.__window,
                ))
            self._cells.append(col_cells)

    def __draw_cells(self):
        if self.__window is None:
            return
        for col in self._cells:
            for cell in col:
                cell.draw()
                self.__animate()

    def __animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        time.sleep(0.05)
