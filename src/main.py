from models.window import Window
from models.point import Point
from models.line import Line


def main():
    win = Window(800, 600)

    line1 = Line(Point(200, 200), Point(500, 400))
    line2 = Line(Point(700, 100), Point(100, 500))

    win.draw_line(line1, "white")
    win.draw_line(line2, "red")

    win.wait_for_close()


main()
