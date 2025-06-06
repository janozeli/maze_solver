from graphics import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "red")
    win.draw_line(Line(Point(800, 0), Point(0, 600)), "red")
    win.wait_for_close()


main()
