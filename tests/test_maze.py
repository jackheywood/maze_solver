import unittest
from models.maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_creates_cells(self):
        # Arrange
        num_cols = 12
        num_rows = 10

        # Act
        maze = Maze(0, 0, num_rows, num_cols, 10)

        # Assert
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )

    def test_maze_positions_cells(self):
        # Arrange
        size = 15

        # Act
        maze = Maze(0, 0, 10, 10, size)

        # Assert
        for x in range(len(maze._cells)):
            for y in range(len(maze._cells[x])):
                cell = maze._cells[x][y]

                self.assertEqual(cell._top_left.x, x * size)
                self.assertEqual(cell._top_left.y, y * size)

                self.assertEqual(cell._top_right.x, x * size + size)
                self.assertEqual(cell._top_right.y, y * size)

                self.assertEqual(cell._bottom_left.x, x * size)
                self.assertEqual(cell._bottom_left.y, y * size + size)

                self.assertEqual(cell._bottom_right.x, x * size + size)
                self.assertEqual(cell._bottom_right.y, y * size + size)

                self.assertEqual(cell._center.x, x * size + size / 2)
                self.assertEqual(cell._center.y, y * size + size / 2)

    def test_maze_breaks_entrance_and_exit(self):
        # Act
        maze = Maze(0, 0, 10, 10, 10)

        # Assert
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[9][9].has_right_wall)

    def test_maze_resets_cells_visited(self):
        # Act
        maze = Maze(0, 0, 10, 10, 10)

        # Assert
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
