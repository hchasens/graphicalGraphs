import turtle

class NodeManager:
    """
    Manages Nodes
    Contains a list of all Nodes and updates them graphicly when they're moved or dragged. Will redraw edges after a node moves.
    Node radius is 10, diamater is 20
    """
    def __init__(self):
        pass

    def createNode():
        """Creates a new Node"""
        pass

    def deleteNode():
        pass

    def createEdge():
        """Creates a new edge between two Nodes"""
        pass

    def moveNode():
        pass

    def isNode():
        pass

    pass

class Test:
    global num
    num = 0
    def __init__(self, num):
        self.num = num
    

class Node:

    def __init__(self, x, y):
        self.selected = False       # is currently selected by the GUI
        self.acvd = False      # is graphicly activated (cuased by an algorithm, not by the user)
        self.loc = (None, None)     # location, tuple, cord
        self.edges = []             # list of connected Nodes
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.shape("circle")
        self.t.color("black")
        self.t.fillcolor('blue')
        self.setLoc((x,y))
        
    def setLoc(self, location: tuple)->bool:
        """Sets Node's Location. Takes tuple (x, y). Returns True if successful"""
        self.loc = location
        try:
            self.t.goto(self.loc)
            return True
        except:
            return False

    def getLoc(self)->tuple:
        """Returns the current location of the node as a tuple"""
        return self.loc

    def selected(self, s: bool):
        """Selects the Node in the GUI. Changes outline to yellow."""
        if s:
            self.selected = True
            self.t.color('yellow')
        else:
            self.selected = False
            self.t.color('black')

    def activated(self, s: bool):
        self.acvd = bool
        self.t.color('red')
        return True


    def addEdge(self, e: 'Node'):
        """Adds an edge to the Node. Takes a Node as an arguement. Returns True if successful."""
        try:
            line = turtle.Turtle()
            line.speed(0)
            line.ht()
            line.penup()
            line.goto(self.getLoc())
            line.pendown()
            line.goto(e.getLoc())
            
            self.edges.append(e)
            e.edges.append(self)
            return True
        except:
            return False


    