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

    def BFS(self,s):

        visited=[False]*(len(self.graph))

        q=[]
        q.append(s)
        visited[s]=True

        while q:
            
            s=q.pop(0)
            print(s,end=' ')

            for i in self.graph[s]:

                if visited[i]==False:
                    q.append(i)
                    visited[i]=True

            


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.BFS(2)

        
