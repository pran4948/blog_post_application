#!/usr/bin/env python
# coding: utf-8
# this is a python script for devloper.
# In[2]:


graph = {'A': ['B', 'D', 'G', 'I'], 
         'B': ['D', 'C'], 
         'C' : ['A', 'E'], 
         'D' : ['F','C'], 
         'E' : ['F', 'J'], 
         'F' : ['H','C'], 
         'G':['F','K'], 
         'H':['E', 'K', 'L'], 
         'I':['S'], 
         'J':['S'], 
         'K':[], 
         'L':['J','F'], 
         'S':['K'] }

print(graph)


# In[8]:


def dfs(graph, source):
    S = list()
    visited_vertices = list()
    S.append(source)
    visited_vertices.append(source)
    while S:
        vertex = S.pop()
        print(vertex, end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                S.append(u)
                visited_vertices.append(u)
 
print("DFS traversal of graph with source 'A' is:")
dfs(graph, 'A')


# In[ ]:




