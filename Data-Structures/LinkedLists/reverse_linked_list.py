"""
Given a linked list, reverse it
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
        def reverse(self):
            curr=self.head
            pre,post=None,None
            while curr:
                post=curr.next
                curr.next=pre
                pre=curr
                curr=post
            self.head=pre
           
            
P=linkedlist()
P.head=node(10)
node2=node(15)
node3=node(20)
node4=node(25)


P.head.next=node2
node2.next=node3
node3.next=node4

print("The list currently is:", end=" ")
P.printlist()
print("After reversal:",end =" ")
P.reverse()
P.printlist()






