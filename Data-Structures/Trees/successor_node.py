"""
Caclulate the succesor of a given node in a binary tree.
"""

class node:
    def __init__(self,val,left=None,right=None):
        self.data=val
        self.left=left
        self.right=right


def leftmost(node):
    while node and node.left:
        node=node.left
    return node
def rightmost(node):
    while node and node.right:
        node=node.right
    return node
def getnext(root,node):
    if not root:
        return None
    if root==node or getnext(root.left,node) or getnext(root.right,node):
        if getnext(root.right,node):
            temp=getnext(root.right,node)
        else:
            temp=getnext(root.left,node)
        if temp:
            if root.left==temp:
                print(root.data)
                return None
        return root
    return None
    


def get_succesor(root,node):
    if node.right:
        print(leftmost(node.right).data)
    elif not node.right:
        if rightmost(root)==node:
            print(node.data)
        else:
            succesor=getnext(root,node)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(6)

get_succesor(root,root.right)