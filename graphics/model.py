import turtle
import node
import tkinter as tk
from algorithms.bfs import *
from algorithms.dfs import *

class Model:
    """
    Abstract interface for Graphical Graphs MVC
    """
    
    # bind left click to 'leftClick'
    # if leftclick not on node, make node
    # else: (clicked on node)
    #       if next click on aother node:
    #               add edge between first and second node
    #       else:
    #           make new node and create edge between first node and last node
    # 


    def __init__(self, screen):
        self.mode = None            # Selected mode by the user (e.g. newNode, deleteNode, addEdge, removeEdge)
        self.ln = [node.Node(0, 0)]
 
        self.screen = screen
        self.screen.onclick(self.leftClick, btn=1)

        self.selected = None
        self.root = self.ln[0]


    def leftClick(self, x, y):
        cur = self.getNode(x,y)     # Find the node that's been clicked on. If there's no node there then cur == None
        #print("Cur: " + cur + "Selected: " + self.selected)

        if cur == None:             # if there's nothing at cur, add a node
            self.addNode(x,y)        
            print("test")
            return

        if self.selected == None:   # if selected == None
            self.selected = cur     # make cur selected
            return
        
        else:                                   # if there is both a selected and a cur
            if self.selected != cur:           # if there is a previously selected node and a newly selected node
                self.selected.addEdge(cur)                      # make an edge between the two
                self.selected = None                            # clear the selected
                return
            else:
                #bfs(cur)
                dfs(cur)
                self.reset()
                return


    def reset(self):
        for n in self.ln:
            n.activated(False)
        self.selected == None

    def getNode(self, x, y):
        "Returns the node at location x, y. If no node is found then returns `None`"
        nRadius = 20            # made twice the size to avoid creating nodes on top of eachother 
        for n in self.ln:
            npos = n.getLoc()
            if abs(npos[0]-x) < 10 and abs(npos[1]-y) < 10:
                return n     
        return None

    def addNode(self, x, y):
        print("node added")
        self.ln.append(node.Node(x, y))

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