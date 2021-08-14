




class Node:

    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data


def insert(root,node):

    if root is None:
        root=node
    else:
        if root.data<node.data:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)

        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)

def inorder(root):

    if root is not None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

root = Node(50) 
insert(root,Node(30)) 
insert(root,Node(20)) 
insert(root,Node(40)) 
insert(root,Node(70)) 
insert(root,Node(60)) 
insert(root,Node(80))

inorder(root)
    
            
