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


def middle(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    return slow.data
        

def mergeSort(head):
    
    if(head==None):
        return None
    if(head.next==None):
        return head

    mid = middle(head)
    head2 = mid.next
    mid.next = None

    head = mergeSort(head)
    head2 = mergeSort(head2)
    head = merge(head, head2)
    return head




if __name__=="__main__":

    l=LinkedList()

    l.app(3)
    l.app(2)
    l.app(1)
    l.app(4)
    l.app(5)

    l=mergeSort(l.head)

    l.printList()
    print()
   
   
