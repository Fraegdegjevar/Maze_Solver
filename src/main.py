# Created by Will Harvey 29/04/2025
from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800,600)
    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)
    c4 = Cell(win)
    c5 = Cell(win)
    
    c1.draw(2,2,102,102)
    c2.has_bottom_wall = False
    c2.draw(102,2,202,102)
    c3.has_left_wall = False
    c3.draw(252,2,352,102)
    c4.has_top_wall = False
    c4.draw(352,2,452,102)
    c5.has_right_wall = False
    c5.draw(452,2,552,102)
    
    c6 = Cell(win)
    c6.draw(300, 310, 700, 550)
    c4.draw_move(c5)
    c5.draw_move(c6, True)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
