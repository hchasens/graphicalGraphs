import turtle
import random
from algorithms.bfs import *
from algorithms.dfs import *
from node import *


ln = []     # list of nodes




def genRanGraph():
    for i in range(-300, 300, 150):
        for k in range(-300, 300, 150):
            ln.append(Node(i,k))
    for i in ln:
        for k in ln:
            if i != k and (random.randint(0,25) == 1):       # 1/15 percent chance any given node has a edge to any other given node
                i.addEdge(k)
        if len(i.edges) == 0:
            i.addEdge(random.choice(ln))


def main():
    c = turtle.Turtle()         # a dumby turlte who's exsistance is to get us the tkinter canvas
    c.ht()

    genRanGraph() 

    #bfs(ln[0])
    dfs(ln[0])

    c.getscreen().exitonclick()
    


if __name__ == "__main__":
    main()
