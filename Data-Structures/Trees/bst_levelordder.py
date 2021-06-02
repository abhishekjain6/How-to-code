"""
Implement level order traversal for a BST.
"""
from collections import deque
q=deque()

class node:
    def __init__(self,val=None,l=None,r=None):
        self.l=l
        self.r=r
        self.val=val

def levelorder(root):
    if root==None:
        return
    q.append(root)
    while(len(q)!=0):
        curr=q.popleft()
        print(curr.val)
        if curr.l:
            q.append(curr.l)
        if curr.r:
            q.append(curr.r)


n1=node(10)
n1.l=node(15)
n1.r=node(20)
n1.l.l=node(25)
n1.r.l=node(30)
n1.r.l.l=node(100)
n1.r.r=node(35)
n1.r.r.l=node(40)
n1.r.r.r=node(45)
levelorder(n1)