from src.include.stack import Stack
import src.windows as win
from tkinter import *

class WindowController(Tk):
    def __init__(self):
        super().__init__()

        self.__root=Stack()
        self.__frame=None
        self.forward(win.FirstPage)

    def forward(self,next):
        newFrame=next(self)
        if self.__frame is not None:
            self.__frame.pack_forget()
        self.__root.push(newFrame)
        self.__frame=newFrame
        self.__frame.pack()

    def backward(self):
        if self.__frame is not None:
            oldFrame=self.__root.pop()
            oldFrame.destroy()
            self.__frame=self.__root.peek()
            self.__frame.pack()