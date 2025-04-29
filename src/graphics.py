# Window class for drawing windows!
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=True)
        self.__running = False # Data member representing whether window is running
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
        
    def draw(self, canvas, fill_colour):
            canvas.create_line(
                self.point1.x, self.point1.y, self.point2.x, self.point2.y, 
                fill=fill_colour, width=2)
        