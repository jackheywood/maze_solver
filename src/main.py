from models.window import Window
from models.cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(win, 200, 200)
    cell2 = Cell(win, 300, 200)
    cell3 = Cell(win, 300, 300)

    cell1.has_right_wall = False
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3.has_top_wall = False

    cell1.draw()
    cell2.draw("red")
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)
    cell1.draw_move(cell3)

    win.wait_for_close()


main()
