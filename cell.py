from line import Line
from point import Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))

        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))

        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))

        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        x_mean = (self.__x1 + self.__x2) / 2
        y_mean = (self.__y1 + self.__y2) / 2
        center_point = Point(x_mean, y_mean)

        other_x_mean = (to_cell.__x1 + to_cell.__x2) / 2
        other_y_mean = (to_cell.__y1 + to_cell.__y2) / 2
        other_center_point = Point(other_x_mean, other_y_mean)

        color = "gray" if undo else "red"
        self.__win.draw_line(Line(center_point, other_center_point), color)
