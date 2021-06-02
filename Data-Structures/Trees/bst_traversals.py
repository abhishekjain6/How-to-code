"""
Implement inorder, preorder and postorfer traversals on a BST.
"""
class node:
    def __init__(self,data=None,l=None,r=None):
        self.val=data
        self.l=l
        self.r=r

def preorder(root):
    if root==None:
        return
    print(root.val)
    preorder(root.l)
    preorder(root.r)
def inorder(root):
    if root==None:
        return
    inorder(root.l)
    print(root.val)
    inorder(root.r)
def postorder(root):
    if root==None:
        return
    postorder(root.l)
    postorder(root.r)
    print(root.val)
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
postorder(n1)
        