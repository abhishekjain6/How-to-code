"""
    Given:
    C, the total weight of backpack
    N, the total number of Items
    W, the weight of item I
    P, the the profit gained by item I
    
    Maximise the profit by putting in any amount of items less than weight C.
"""


n=10
c=78
w=[10,10,12,12,12,12,12,15,15,15]
p=[12,12,15,15,15,15,15,14,14,14]


def knapsack(c,n,w,p): ##Getting the max profit
    if c==0 or n==0:
        return(0)
    elif w[n-1]>c:
        return((knapsack(c,n-1,w,p)))
    else:
        return(max(p[n-1]+knapsack(c-w[n-1],n-1,w,p),knapsack(c,n-1,w,p)))

knapsack(c,n,w,p)    
