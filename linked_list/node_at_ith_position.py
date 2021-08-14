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



class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def push(self,new_data):

        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def app(self,new_data):

        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return

        last=self.head

        while last.next:
            last=last.next

        last.next=new_node

    def printList(self):

        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        

    def length(self):

        temp=self.head

        c=0
        while temp:
            c+=1
            temp=temp.next

        print()
        print(c)

    def ithNode(self,i):

        temp=self.head
        c=0
        while (temp and c!=i):
            c+=1
            temp=temp.next
        if c==i:
            return temp.data
        else:
            return None

def delete(head,i):

    temp=head
    c=0
    while temp and c!=i:
        c+=1
        temp=temp.next
    if c==i:
        temp.data=temp.next.data
        temp.next=temp.next.next
    return temp

if __name__=="__main__":

    l=LinkedList()

    l.push(3)
    l.push(2)
    l.push(1)
    l.app(4)
    l.app(5)
   

    l.printList()
    print()
   
    delete(l.head,2)
    l.printList()
