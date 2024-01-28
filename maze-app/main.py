from tkinter import Tk, BOTH, Canvas
import time


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "black")
        else:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "white")

        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "black")
        else:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "black")
        else:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "black")

        else:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            line = Line(point_1, point_2)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if undo is False:
            color = "red"
        else:
            color = "gray"
        start_center_x = int((self._x1 + self._x2) / 2)
        start_center_y = int((self._y1 + self._y2) / 2)
        end_center_x = int((to_cell._x1 + to_cell._x2) / 2)
        end_center_y = int((to_cell._y1 + to_cell._y2) / 2)

        start_point = Point(start_center_x, start_center_y)
        end_point = Point(end_center_x, end_center_y)
        line = Line(start_point, end_point)
        self._win.draw_line(line, color)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_class()

    def _create_class(self):
        # self._cells = [[Cell(win) for col in range(self.num_cols)] for row in range(self.num_rows)]
        self._cells = []
        for col in range(self.num_cols):
            column_cells = []
            for row in range(self.num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)

        # Drawing
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.cell_size_x * i + self._x1
        y1 = self.cell_size_y * j + self._y1
        x2 = self.cell_size_x + x1
        y2 = self.cell_size_y + y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[-1][-1]
        top_left_cell.has_left_wall = False
        bottom_right_cell.has_right_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


#
# win = Window(800, 600)
# nums_rows = 12
# num_cols = 10
# m1 = Maze(0, 0, nums_rows, num_cols, 10, 10, win)
# m1._break_entrance_and_exit()
# win.wait_for_close()
