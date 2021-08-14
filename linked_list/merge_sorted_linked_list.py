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

    def middle(self):

        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.data

def merge(head1,head2):

    if head1==None:
        return head2

    if head2==None:
        return head1

    if head1.data<head2.data:
        head=head1
        head1=head1.next

    else:
        head=head2
        head2=head2.next

    curr=head

    while head1 and head2:

        if head1.data<=head2.data:
            curr.next=head1
            head1=head1.next
        else:
            curr.next=head2
            head2=head2.next
        curr=curr.next

    if head1==None:
        curr.next=head2
    else:
        curr.next=head1

    return head


def printList(head):
    temp=head
    while temp:
        print(temp.data,end=' ')
        temp=temp.next
        

        
if __name__=="__main__":

    l1=LinkedList()
    l2=LinkedList()

        
    l1.app(1)
    l1.app(2)
    l1.app(3)
    l1.app(4)
    l1.app(5)

    l2.app(6)
    l2.app(7)
    l2.app(8)
    l2.app(9)
    l2.app(10)

    
    merge(l1.head,l2.head)
    printList(l1.head)
    
    
