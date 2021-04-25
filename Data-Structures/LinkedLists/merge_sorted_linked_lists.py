"""
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
your program can change in a node is its next field.
Output list should also be sorted
"""

class node:
    def __init__(self,val):
            self.val=val
            self.next=None
class linkedlist:
        def __init__(self):
                self.head=None
        def insert(self,nde,newnode):
                newnode.next=nde.next
                nde.next=newnode
        def push(self,nde):
                nde.next=self.head
                self.head=nde
        def delete(self,nde):
                nde.next=nde.next.next
        def search(self,N):
                p=self.node
                while p.next!=None:
                        if p.val==N:
                                return(True)
                        p=p.next
                return(False)
        def printlist(self):
                p=self.head
                while p!=None:
                        print(p.val,end=" ")
                        p=p.next
                print()


def merge(a,b):
    a=a.head
    b=b.head
    sortedlist=linkedlist()
    if a.val<=b.val:
        p=a
        a=a.next
    else:
        p=b
        b=b.next
    sortedlist.head=p
    while b or a:
        if a==None:
            p.next=b
            b=b.next
        elif b==None:
            p.next=a
            a=a.next
        elif a.val<=b.val:
            p.next=a
            a=a.next
        else:
            p.next=b
            b=b.next
        p=p.next
    return(sortedlist)

    
P1=linkedlist()
P1.head=node(10)
node2=node(15)
node3=node(20)
node4=node(25)


P1.head.next=node2
node2.next=node3
node3.next=node4


P2=linkedlist()
P2.head=node(7)
node5=node(12)
node6=node(18)
node7=node(30)

P2.head.next=node5
node5.next=node6
node6.next=node7

P1.printlist()
P2.printlist()


L=merge(P1,P2)
L.printlist()

