"""
Write a program to find the depth and height of a node in a given bst.
"""
height=-1
class node:
    def __init__(self,val=None,right=None,left=None):
        self.val=val
        self.l=left
        self.r=right
def getdep(root,val):
    if root==None:
        return(-1)
    dist=-1
    if root.val==val:
        return(dist+1)
    dist=getdep(root.l,val)
    if dist>=0:
        return(dist+1)
    dist=getdep(root.r,val)
    if dist>=0:
        return(dist+1)
    return dist
def getheight(root,val):
    global height
    if root==None:
        return(-1)
    lh=getheight(root.l,val)
    rh=getheight(root.r,val)
    ans=max(lh,rh)+1
    #print(root.val)
    if root.val==val:
        height=ans
    return(ans)
def getheightofnode(root,val):
    global height
    maxdep=getheight(root,val)
    return(height)

n1=node(10)
n1.l=node(15)
n1.r=node(20)
n1.l.l=node(25)
n1.r.l=node(30)
n1.r.l.l=node(100)
n1.r.r=node(35)
n1.r.r.l=node(40)
n1.r.r.r=node(45)
n1.r.r.r.l=node(11)
print(getdep(n1,15))
print(getheightofnode(n1,20))
