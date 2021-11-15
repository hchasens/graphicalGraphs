from node import *
import time

def dfs(root: Node):
    root.activated(True)
    for v in root.edges:
        if not v.acvd:
            dfs_visit(v, root)

def dfs_visit(cur: Node, root: Node):
    time.sleep(0.8)
    cur.activated(True)             # traversed this new node
    for v in cur.edges:             # for all of the current nodes edges
        if not v.acvd:              # if one is not traversed
            dfs_visit(v, cur)       # traverse it with the current node as the parrent
    pass