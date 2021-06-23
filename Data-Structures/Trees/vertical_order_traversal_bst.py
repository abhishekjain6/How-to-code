"""
Given pointer to the root node, print the binary tree in vertical order.
"""
from collections import deque
dist={}


class node:
    def __init__(self,val=None,l=None,r=None):
        self.val=val
        self.l=l
        self.r=r
        self.hd=0
def vert(root,cd,dist):
    if not root:
        return
    p=deque()
    p.append(root)
    while(len(p)):
        root=p[0]
        cd=root.hd
        if cd not in dist:
            dist[cd]=root.val
        if root.l:
            root.l.hd=cd-1
            p.append(root.l)
        if root.r:
            root.r.hd=cd+1
            p.append(root.r)
        p.popleft()
    for x in sorted(list(dist.keys())):
        print(dist[x])
    



head=node(1)
head.l=node(2)
head.r=node(3)
head.l.r=node(4)
head.l.r.r=node(5)
head.l.r.r.r=node(6)

#printvert(head)


vert(head,0,dist)