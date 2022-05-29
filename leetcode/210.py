from collections import defaultdict
class graph:
    def __init__(self,numCourses):
        self.graph=defaultdict(list)
        self.numCourses=numCourses
        

    def addEdge(self,src,dst):
        self.graph[src].append(dst)

    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        
        stack.append(v)

    def topologicalSort(self):
        visited=[False]*(self.numCourses)
        stack=[]

        for i in range(self.numCourses):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        return stack

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
        visited=[False]*(self.numCourses)
        stack=[False]*(self.numCourses)
        
        for i in range(self.numCourses):
            if visited[i]==False:
                if self.isCyclicUtil(i,visited,stack)==True:
                    return True
        return False

    
class Solution:
    def findOrder(self, numCourses, prerequisites):
        g=graph(numCourses)

        for edge in prerequisites:
            g.addEdge(edge[0],edge[1])
        
        if g.isCyclic()==True:
            return []
        
        return g.topologicalSort()

s=Solution()
numCourses=2
prerequisites=[[0,1]]

# numCourses=4
# prerequisites=[[1,0],[2,0],[3,1],[3,2]]
#[0,2,1,3]

print(s.findOrder(numCourses,prerequisites))


# Input:
# 2
# [[1,0]]
# 2
# [[0,1]]
# 4
# [[1,0],[2,0],[3,1],[3,2]]
# 1
# []
# 2
# []
# 2
# [[0,1],[1,0]]
# 3
# [[2,1],[1,0]]

# Output:
# [0,1]
# [1,0]
# [0,2,1,3]
# [0]
# [1,0]
# []
# [0,1,2]