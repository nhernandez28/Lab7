"""
Lab 7
Created on Apr 27, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

import numpy as np
from queue import *

def BFS(G, v):
    visited = np.full(len(G), False, dtype = bool)
    prev = np.full(len(G), -1, dtype = int)
    #creates new queue
    queue = Queue(maxsize = 0)
    queue.put(v)
    
    while not queue.empty():
        u = queue.get()
        for t in G[u]:
            #if not yet been visited
            if not visited[t]:
                #marks vertex as visited
                visited[t] = True
                #gets next u
                prev[t] = u
                queue.put(t)
                
    return prev

#Depth-first search using a stack. This is identical to breadth-first search but the queue is replaced
#by a stack    
def DFSStack(G, start):
    visited = np.full(len(G), False, dtype = bool)
    #empty stack
    stack = []
    prev = np.full(len(G), -1, dtype = int)
    
    stack.append(start)
    
    while len(stack) > 0:
        #pops the last one
        u = stack.pop(-1)
        
        #goes to every vertex that u points to
        for i in G[u]:
            
            #if it is not yet been visited
            if not visited[i]:
                #marks that vertex as visited
                visited[i] = True
                #moves on to next u
                prev[i] = u
                #adds to stack
                stack.append(i)
            
    return prev

#Depth-fist search using recursion
def DFSRecursion(G, vertex, visited):
    #if vertex has not yet been visited
    if vertex not in visited:
        #adds vertex to visited list
        visited.append(vertex)
        
        #goes to every verted that the previous points to
        for i in G[vertex]:
            DFSRecursion(G, i, visited)
            
    return visited