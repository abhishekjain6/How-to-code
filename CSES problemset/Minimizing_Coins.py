n,x=map(int,input().split())
arr=list(map(int,input().split()))
dp=[10**6+1]*(x+1)
dp[0]=0
for y in range(1,x+1):
    for z in arr:
        if y-z>=0:
            dp[y]=min(dp[y],dp[y-z]+1)
print(dp[x]) if dp[x]!=10**6+1 else print("-1") 