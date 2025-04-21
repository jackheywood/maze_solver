from models.line import Line
from models.point import Point


class Cell:
    def __init__(self, x, y, size=50, window=None):
        self._top_left = Point(x, y)
        self._top_right = Point(x + size, y)
        self._bottom_left = Point(x, y + size)
        self._bottom_right = Point(x + size, y + size)
        self._center = Point(x + size / 2, y + size / 2)
        self.__window = window
        self.visited = False
        self.__init_walls()

    def __init_walls(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, line_color="white", bg_color="black"):
        if self.__window is None:
            return
        self.__window.draw_line(
            Line(self._top_left, self._bottom_left),
            line_color if self.has_left_wall else bg_color,
        )
        self.__window.draw_line(
            Line(self._top_left, self._top_right),
            line_color if self.has_top_wall else bg_color,
        )
        self.__window.draw_line(
            Line(self._top_right, self._bottom_right),
            line_color if self.has_right_wall else bg_color,
        )
        self.__window.draw_line(
            Line(self._bottom_left, self._bottom_right),
            line_color if self.has_bottom_wall else bg_color,
        )

    def draw_move(self, to_cell, undo=False):
        self.__window.draw_line(
            Line(self._center, to_cell._center),
            "gray" if undo else "red",
        )
