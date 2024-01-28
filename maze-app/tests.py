import unittest

from main import Maze, Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        nums_rows = 12
        num_cols = 10
        m1 = Maze(0, 0, nums_rows, num_cols, 10, 10, win)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), nums_rows)

    def test_break_and_exit(self):
        win = Window(800, 600)
        nums_rows = 12
        num_cols = 10
        m1 = Maze(0, 0, nums_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(
            m1._cells[len(m1._cells) - 1][len(m1._cells[0]) - 1].has_right_wall, False
        )


if __name__ == "__main__":
    unittest.main()
