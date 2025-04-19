from models.line import Line
from models.point import Point


class Cell:
    def __init__(self, window, x, y, size=50):
        self._top_left = Point(x, y)
        self._top_right = Point(x + size, y)
        self._bottom_left = Point(x, y + size)
        self._bottom_right = Point(x + size, y + size)
        self._center = Point(x + size / 2, y + size / 2)
        self.__window = window
        self.__init_walls()

    def __init_walls(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color="white"):
        if self.has_left_wall:
            self.__window.draw_line(
                Line(self._top_left, self._bottom_left),
                fill_color,
            )
        if self.has_top_wall:
            self.__window.draw_line(
                Line(self._top_left, self._top_right),
                fill_color,
            )
        if self.has_right_wall:
            self.__window.draw_line(
                Line(self._top_right, self._bottom_right),
                fill_color,
            )
        if self.has_bottom_wall:
            self.__window.draw_line(
                Line(self._bottom_left, self._bottom_right),
                fill_color,
            )

    def draw_move(self, to_cell, undo=False):
        self.__window.draw_line(
            Line(self._center, to_cell._center),
            "gray" if undo else "red",
        )
