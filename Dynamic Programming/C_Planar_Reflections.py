"""
https://codeforces.com/contest/1498/problem/C
"""
for _ in range(int(input())):
    n,k=map(int,input().split())
    MOD=1000000007
    dp=[[0 for x in range(1010)] for y in range(1010)]
    for l in range(k+1):
        for m in range(n+1):
            if l==1:
                dp[l][m]=1
            elif m==0:
                dp[l][m]=1
            else:
                dp[l][m]=(dp[l][m-1]+dp[l-1][n-m])%MOD
    print(dp[k][n])

    