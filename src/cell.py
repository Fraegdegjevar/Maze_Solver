from graphics import Line, Point, Window

class Cell:
    def __init__(self, win): #centre x and x
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2, colour="black"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), colour)
        
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), colour)

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y2), Point(self._x1, self._y2)), colour)

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x1, self._y1)), colour)
    
    def draw_move(self, to_cell, undo=False):
        move = Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), 
                    Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2))
        if undo == False:
            colour = "red"
        else:
            colour = "grey"
        
        self._win.draw_line(move, colour)