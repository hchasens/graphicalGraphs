import turtle
from tkinter import *
import graphics.model as md

class Controller:

    def __init__(self, t: turtle, ln: list):

        self.screen = turtle.Screen()
        self.canvas = self.screen.getcanvas()
        self.screen.title("A Turtle Graphics Screen")
        self.screen.setup(700, 700)
        
        self.ln = ln
        self.model = md.Model(self.screen)
        self.setup()
        pass


    def setup(self):
        #self.addNodeButton = Button(self.canvas.master, text="Add Node", command=self.screen.onclick(self.model.addNode))
        self.addNodeButton = Button(self.canvas.master, text="Add Node", command=self.screen.onclick(print("add selected")))
        self.addNodeButton.pack(side=LEFT)
        #self.canvas.create_window(-200, -200, window=self.addNodeButton)

        self.rmNodeButton = Button(self.canvas.master, text="Remove Node", command=self.screen.onclick(self.model.rmNode))
        self.rmNodeButton.pack(side=LEFT)
        #self.canvas.create_window(-200, -100, window=self.rmNodeButton)
        
    pass