'''

Given a linked list, find and return the length of input LL. Do it iteratively.
Input format :
Linked list elements (separated by space and terminated by -1)
Output format :
Length of LL
Sample Input :
3 4 5 2 6 1 9 -1
Sample Output :
7

'''


from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph=defaultdict(list)

    def addEdge(self,u,v):#function to add an edge to graph
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):#function used by DFS   

        visited[v]=True
        print(v,end=' ')#Mark the current node as visited and print it


        for i in self.graph[v]:#recur for all the vertices adjacent to this vertex

            if visited[i]==False:
                self.DFSUtil(i,visited)

    def DFS(self,v):#function to do DFS Traversal

        visited=[False]*(len(self.graph))

        self.DFSUtil(v,visited)


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)

        
