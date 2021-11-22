import turtle
import node
import tkinter as tk


class Model:
    """
    Abstract interface for Graphical Graphs MVC
    """
    

    def __init__(self, screen):
        self.mode = None            # Selected mode by the user (e.g. newNode, deleteNode, addEdge, removeEdge)
        self.ln = [node.Node(0, 0)]


    def getNode(self, x, y):
        "Returns the node at location x, y. If no node is found then returns `None`"
        nRadius = 10
        for n in self.ln:
            npos = n.getLoc()
            if (npos[0]-x < 10 or x-npos[0] < 10) and (npos[1]-y < 10 or y-npos[1] < 10):
                return n     
        return None



    def addNode(self, x, y):
        print("node added")
        self.ln.append(node.Node(x, y))
        self.screen.onclick(None)

    def rmNode(self, x, y):
        print("node removed")
        """removes Node at x,y. Returns 1 is sucessfull, 0 if not"""
        try:
            n = self.getNode(x, y)
            if n != None:
                n.ht()
                self.ln.remove(n)
                return 1
        except:
            return 0
        self.screen.onclick(None)

