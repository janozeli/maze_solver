from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    Cell(win).draw(100, 100, 700, 500)
    win.wait_for_close()


main()
