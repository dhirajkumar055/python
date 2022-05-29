#BFS - Queue

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,src,dst):
        self.graph[src].append(dst)
    
    def BFS(self,v):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(v)
        visited[v]=True

        while queue:
            curr=queue.pop(0)
            print(curr,"->",end=' ')
            for i in self.graph[curr]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

    def DFSUtils(self,v,visited):
        visited[v]=True
        print(v,"->",end=' ')
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtils(i,visited)

    def DFS(self,v):
        visited=[False]*len(self.graph)

        self.DFSUtils(2,visited)
        for i in self.graph:
            if visited[i]==False:
                self.DFSUtils(i,visited)
    
    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        stack.append(v)

    def topologicalSort(self):
        visited=[False]*len(self.graph)
        stack=[]

        for i in range(len(self.graph)):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        
        print(stack)

    def isCyclicUtil(self,v,visited,stack):
        visited[v]=True
        stack[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,stack)==True or stack[i]==True:
                    return True
            elif stack[i]==True:
                return True

        stack[v]=False
        return False

    def isCyclic(self):
        visited=[False]*(len(self.graph))
        stack=[False]*(len(self.graph))
        for i in range(len(self.graph)):
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,stack)==True:
                    return True
        return False


    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# g.DFS(2)
g.topologicalSort()

# DFS:
# 1) Detecting cycle in a graph
# 2) Path Finding
# 3) Topological Sorting
# 4) To test if a graph is bipartite
# 5) Finding Strongly Connected Components of a graph
# 6) Solving puzzles with only one solution, such as mazes

# BFS
# 1) Shortest Path and Minimum Spanning Tree for unweighted graph
# 2) Peer to Peer Networks
# 3) Crawlers in Search Engines
# 4) Social Networking Websites
# 5) GPS Navigation systems
# 6) Broadcasting in Network
# 7) In Garbage Collection
# 8) Cycle detection in undirected graph
# 9) Ford–Fulkerson algorithm 
# 10) To test if a graph is Bipartite 
# 11) Path Finding 
# 12) Finding all nodes within one connected component

