"""
Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf
paths.
"""
class node:
    def __init__(self,data=None,l=None,r=None):
        self.val=data
        self.l=l
        self.r=r
def binarysum(root,csum):
    if root==None:
        return
    csum*=2
    csum+=root.val
    if not root.l and not root.r:
        return(csum)
    return(binarysum(root.l,csum)+binarysum(root.r,csum))





head=node(1)
head.l=node(0)
head.l.l=node(1)
head.l.r=node(0)
head.l.l.l=node(0)
head.l.l.r=node(0)
head.r=node(1)
head.r.l=node(0)
head.r.r=node(1)
head.r.r.l=node(1)
head.r.r.r=node(0)
print(binarysum(head,0))
