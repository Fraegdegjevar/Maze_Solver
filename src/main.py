# Created by Will Harvey 29/04/2025
from graphics import Window, Point, Line

def main():
    win = Window(800,600)
    p1 = Point(5,5)
    p2 = Point(500,590)
    line = Line(p1, p2)
    p3 = Point(69, 402)
    p4 = Point(721, 102)
    line2 = Line(p3,p4)
    win.draw_line(line, fill_colour="red")
    win.draw_line(line2, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
