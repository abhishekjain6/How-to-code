n,x=map(int,input().split())
arr=list(map(int,input().split()))
dp=[0]*(x+1)
dp[0]=1
for y in range(1,x+1):
    for z in arr:
        if y-z>=0:
            dp[y]+=dp[y-z]
            dp[y]%=(10**9+7)
print(dp[x]) 