import random
import time
from enum import Enum
from models.cell import Cell


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Maze:
    def __init__(self, x, y, rows, cols, cell_size, window=None, seed=None):
        self.__x = x
        self.__y = y
        self.__rows = rows
        self.__cols = cols
        self.__cell_size = cell_size
        self.__window = window

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__draw_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        return self.__solve_recursive(0, 0)

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
                self.__draw_cell(cell)

    def __draw_cell(self, cell):
        if self.__window is None:
            return
        cell.draw()
        self.__animate()

    def __break_entrance_and_exit(self):
        # Break top left wall
        top_left_cell = self._cells[0][0]
        top_left_cell.has_left_wall = False
        self.__draw_cell(top_left_cell)

        # Break bottom right wall
        top_right_cell = self._cells[self.__cols - 1][self.__rows - 1]
        top_right_cell.has_right_wall = False
        self.__draw_cell(top_right_cell)

    def __break_walls(self, start_x, start_y):
        cell_stack = [(start_x, start_y)]

        while cell_stack:
            (x, y) = cell_stack.pop()
            current_cell = self._cells[x][y]
            current_cell.visited = True
            neighbours = self.__get_valid_neighbours(x, y)

            if len(neighbours) == 0:
                self.__draw_cell(current_cell)
                continue
            else:
                cell_stack.append((x, y))

            direction = random.choice(list(neighbours.keys()))

            (next_x, next_y) = neighbours[direction]
            cell_stack.append((next_x, next_y))
            next_cell = self._cells[next_x][next_y]

            self.__break_walls_between_cells(direction, current_cell, next_cell)

    def __get_valid_neighbours(self, x, y, check_walls=False):
        directions = {}
        current = self._cells[x][y]
        if (
                x - 1 >= 0 and not self._cells[x - 1][y].visited
                and (not check_walls or not current.has_left_wall)
        ):
            directions[Direction.LEFT] = (x - 1, y)
        if (
                x + 1 < self.__cols and not self._cells[x + 1][y].visited
                and (not check_walls or not current.has_right_wall)
        ):
            directions[Direction.RIGHT] = (x + 1, y)
        if (
                y - 1 >= 0 and not self._cells[x][y - 1].visited
                and (not check_walls or not current.has_top_wall)
        ):
            directions[Direction.UP] = (x, y - 1)
        if (
                y + 1 < self.__rows and not self._cells[x][y + 1].visited
                and (not check_walls or not current.has_bottom_wall)
        ):
            directions[Direction.DOWN] = (x, y + 1)
        return directions

    @staticmethod
    def __break_walls_between_cells(direction, current_cell, next_cell):
        match direction:
            case Direction.UP:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            case Direction.DOWN:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            case Direction.LEFT:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            case Direction.RIGHT:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            case _:
                raise Exception(f"Invalid direction {direction}")


    def __solve_recursive(self, x, y):
        self.__animate()
        if x == self.__cols - 1 and y == self.__rows - 1:
            return True
        current_cell = self._cells[x][y]
        current_cell.visited = True

        neighbours = self.__get_valid_neighbours(x, y, True)
        coordinates = list(neighbours.values())
        random.shuffle(coordinates)

        for (x, y) in coordinates:
            next_cell = self._cells[x][y]
            current_cell.draw_move(next_cell)
            if self.__solve_recursive(x, y):
                return True
            current_cell.draw_move(next_cell, True)

        return False


    def __reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def __animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        time.sleep(0.01)
