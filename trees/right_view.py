import collections



class Node:

    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data



def rightview(root):

    q=collections.deque()

    split=[]

    if not root:

        return []

    q.append(root)

    while(q):

        level=[]

        for _ in range(len(q)):

            curr=q.popleft()

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

            level.append(curr.data)
        split.append(level)


    final=[]

    for i in split:
        final.append(i[-1])

    return final,split



  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
print(rightview(root)) 
  

        
    

            

                
