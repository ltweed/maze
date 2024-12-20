from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            print("Window is not set.")
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        s1 = (self._x1 + self._x2) // 2
        print(f"self._x1: {self._x1}, self._x2: {self._x2}, s1: {s1}")
        s2 = (self._y1 + self._y2) // 2
        print(f"self._y1: {self._y1}, self._y2: {self._y2}, s2: {s2}")
        o1 = (to_cell._x1 + to_cell._x2) // 2
        print(f"to_cell._x1: {to_cell._x1}, to_cell._x2: {to_cell._x2}, o1: {o1}")
        o2 = (to_cell._y1 + to_cell._y2) // 2
        print(f"to_cell._y1: {to_cell._y1}, to_cell._y2: {to_cell._y2}, o2: {o2}")

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(s1, s2), Point(o1, o2))
        self._win.draw_line(line, fill_color)
