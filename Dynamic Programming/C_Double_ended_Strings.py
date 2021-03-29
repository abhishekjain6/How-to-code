"""
https://codeforces.com/contest/1506/problem/C
"""



def lcr(a,b,m,n):
    dp=[[0 for x in range(n+2)] for y in range(m+2)]
    res=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                res=max(res,dp[i][j])
            else:
                dp[i][j]=0
    return(res)
for _ in range(int(input())):
    a=input()
    b=input()
    m=len(a)
    n=len(b)
    print(m+n-2*lcr(a,b,m,n))