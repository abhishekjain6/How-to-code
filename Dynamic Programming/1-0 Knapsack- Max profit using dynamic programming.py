"""
    Given:
    C, the total weight of backpack
    N, the total number of Items
    W, the weight of item I
    P, the the profit gained by item I
    
    Maximise the profit by putting in any amount of items less than weight C.
"""





def knapsack_dp(c,n,q,p): ##Getting objects using dynamic programming
    table=[[0 for x in range (c+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(c+1):
            if i==0 or j==0:
                table[i][j]=0
            elif w[i-1]<=j:
                table[i][j]=max(p[i-1]+table[i-1][j-w[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table[n][c]
n=10
c=78
w=[10,10,12,12,12,12,12,15,15,15]
p=[12,12,15,15,15,15,15,14,14,14]
knapsack_dp(c,n,w,p)