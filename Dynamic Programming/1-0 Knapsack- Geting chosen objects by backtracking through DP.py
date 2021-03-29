"""
    Given:
    C, the total weight of backpack
    N, the total number of Items
    W, the weight of item I
    P, the the profit gained by item I
    
    Maximise the profit by putting in any amount of items less than weight C. Print out the selected objects.
"""



n=4
c=60
w=[20, 10, 40, 30]
p=[40, 100, 50, 60]

def knapsack_dp_objects(c,n,q,p): ##Getting objects using dynamic programming
    table=[[0 for x in range (c+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(c+1):
            if i==0 or j==0:
                table[i][j]=0
            elif w[i-1]<=j:
                table[i][j]=max(p[i-1]+table[i-1][j-w[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    maxprofit= table[n][c]
    i=n
    print(table[n][c])
    while i>0 and maxprofit>0:
        if maxprofit!=table[i-1][c]:
            print(w[i-1],end=" ")
            maxprofit=maxprofit-p[i-1]
            c-=w[i-1]
        i-=1 
knapsack_dp_objects(c,n,w,p)