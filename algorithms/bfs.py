from node import *
import time

def bfs(cur: Node):
    cur.activated(True)
    q = [cur]                       #   enqueue
    while len(q) != 0:              #   while the queue isn't empty
        time.sleep(0.8)     # time delay for easier visualization
        u = q.pop(0)                #   dequeue     Take the first element
        u.activated(True)           #   marks the node as haven been traversed
        for v in u.edges:
            if not v.acvd:          #   find all it's unfound edges
                q.append(v)         #   add that edge to the queue enqueue
        
    

