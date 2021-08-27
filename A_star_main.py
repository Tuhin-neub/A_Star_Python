# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:41:54 2021

@author: TUHIN
"""

v = int(input("Enter the vertex: "))
edg = int(input("Enter the edge: "))

adj_list = {}

for i in range(edg):
    st = input("Enter the start: ")
    en = input("Enter the end: ")
    cost = int(input("Enter cost: "));
    
    if adj_list.get(st) == None:
        adj_list[st] = []
    if adj_list.get(en) == None:
        adj_list[en] = []
        
    adj_list[st].append([cost,en])
    adj_list[en].append([cost,st])

print(adj_list)

#Initialization
def initialize(visited,parent):
    
    for key in adj_list.keys():
        visited[key] = False
        parent[key] = None
        
    #print(visited)
    
    #print(parent)
    
def print_path(parent,node):
    if node == None:
        return
    print_path(parent,parent[node])
    print(node)
    
from queue import PriorityQueue
st = input("Enter start node: ")
goal = input("Enter goal node: ")

print("Enter heuristic (sdl) value: ")
h = {}
for key in adj_list.keys():
    h[key] = (int(input(f"h({key}): ")))
print(h)


visited = {}
parent = {}
initialize(visited,parent)

q = PriorityQueue()
q.put([0+h[st],st])
while not q.empty():
    cost,node = q.get()
    print (f"{node}:| f={cost},g={cost-h[node]},h={h[node]}")
    cost -= h[node]
    visited[node] = True
    
    if node == goal:
        print_path(parent,node)
        break
        
    for data in adj_list[node]:
        cld_cost,child = data
        
        if not visited[child]:
            cld_cost += (cost + h[child] ) 
            q.put([cld_cost,child])
            parent[child] = node