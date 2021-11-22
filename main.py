import turtle
import random
from algorithms.bfs import *
from algorithms.dfs import *
from node import *
import graphics.controller as ctl
from graphGen import *



def main():
    ln = []     # list of nodes

    c = turtle.Turtle()         # a dumby turlte who's exsistance is to get us the tkinter canvas
    c.ht()

    genRanGraph(ln)

    bfs(ln[0])

    controller = ctl.Controller(c, ln)


    c.getscreen().mainloop()
    


if __name__ == "__main__":
    main()
