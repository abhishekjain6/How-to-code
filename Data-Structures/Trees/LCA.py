"""
Given two nodes, find their lowest common ancestor.
"""

class node:
    def __init__(self,val=None,r=None,l=None):
        self.val=val
        self.r=r
        self.l=l

def lca(root,v1,v2):
    if root==None:
        return None
    if root.val==v1 or root.val==v2:
        return root
    
    l=lca(root.l,v1,v2)
    r=lca(root.r,v1,v1)

    if l and r:
        return(root)
    return l if l else r


n1=node(10)
n1.l=node(15)
n1.r=node(20)
n1.l.l=node(25)
n1.l.r=node(50)
n1.r.l=node(30)
n1.r.l.l=node(100)
n1.r.r=node(35)
n1.r.r.l=node(40)
n1.r.r.r=node(45)
print(lca(n1,25,50).val)