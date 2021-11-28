import turtle
import random
from algorithms.bfs import *
from algorithms.dfs import *
from node import *
import graphics.controller as ctl
from graphGen import *
import graphics.model as model


def main():
    ln = []     # list of nodes

    c = turtle.Turtle()         # a dumby turlte who's exsistance is to get us the tkinter canvas
    c.ht()
    screen = c.getscreen()

    m = model.Model(screen)


    #genRanGraph(ln)

    # bind left click to 'leftClick'
    # if leftclick not on node, make node
    # else: (clicked on node)
    #       if next click on aother node:
    #               add edge between first and second node
    #       else:
    #           make new node and create edge between first node and last node
    # 

    screen.mainloop()
    


if __name__ == "__main__":
    main()
