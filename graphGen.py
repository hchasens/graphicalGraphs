
from node import *
import random



def genRanGraph(ln: list):
    for i in range(-300, 300, 150):
        for k in range(-300, 300, 150):
            ln.append(Node(i,k))
    for i in ln:
        for k in ln:
            if i != k and (random.randint(0,25) == 1):       # 1/15 percent chance any given node has a edge to any other given node
                i.addEdge(k)
        if len(i.edges) == 0:
            i.addEdge(random.choice(ln))