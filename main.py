from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell_a = Cell(win)
    cell_b = Cell(win)
    cell_a.draw(100, 50, 200, 150)
    cell_b.draw(300, 100, 600, 300)
    cell_a.draw_move(cell_b)
    cell_b.draw_move(cell_a, undo=True)
    win.wait_for_close()


main()
