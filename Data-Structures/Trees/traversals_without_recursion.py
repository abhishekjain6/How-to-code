"""
Write functions to implement preorder, inorder and postorder traversals 
without recursion.
"""

class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def inorder(root):
    res=[]
    rec_stack=[]

    while rec_stack or root:
        if root:
            rec_stack.append(root)
            root=root.left
        else:
            root=rec_stack.pop()
            res.append(root.val)
            root=root.right
    return(res)

def preorder(root):
    res=[]
    rec_stack=[root]

    while rec_stack:
        curr=rec_stack.pop()
        if curr:
            res.append(curr.val)
            rec_stack.append(curr.right)
            rec_stack.append(curr.left)
    return(res)

def postorder(root):
    res=[]
    rec_stack=[root]
    while rec_stack:
        curr=rec_stack.pop()
        res.append(curr.val)
        if curr.left:
            rec_stack.append(curr.left)
        if curr.right:
            rec_stack.append(curr.right)
    return(res[::-1])



n1=node(10)
n1.right=node(45)
n1.left=node(15)
n1.left.left=node(25)
n1.left.right=node(30)
print(*inorder(n1))
print(*preorder(n1))
print(*postorder(n1))