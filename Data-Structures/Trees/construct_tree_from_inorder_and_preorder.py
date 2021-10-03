"""
Given 2 lists of preorder and inorder traversal, construct the tree corresponding to both of them.
"""

class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def build(inor,pre,start,stop):
    global mp,initindex

    if start>stop:
        return None
    
    curr=pre[initindex]
    initindex+=1
    n=node(curr)

    if start==stop:
        return n

    idx=mp[curr]
    n.left=build(inor,pre,start,idx-1)
    n.right=build(inor,pre,idx+1,stop)
    return n


def buildmap(inor,pror,start,stop):
    global mp
    for x in range(len(inor)):
        mp[inor[x]]=x
    return build(inor,preorder,start,stop)

def inorder_trav(node):
    if node==None:
        return
    inorder_trav(node.left)
    print(node.val,end=" ")
    inorder_trav(node.right)



mp={}
initindex=0
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']



head=buildmap(inorder,preorder,0,len(inorder)-1)
inorder_trav(head)
