from sys import stdin
input = stdin.readline
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as c,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log,inf
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 




def solve():
    n=ii()
    arr=li()
    arr1=[0]
    arr2=[0]
    for x in range(n):
        if arr[x]==1:
            arr1.append(x+1)
        else:
            arr2.append(x+1)
    #print(arr1)
    #print(arr2)
    dp=[[0 for y in range(len(arr2))] for x in range(len(arr1))]
    s1,s2=len(arr1),len(arr2)
    for x in range(s1):
        for y in range(s2):
            dp[x][y]=inf
    for x in range(s2):
        dp[0][x]=0
    ans=inf
    for x in range(1,s1):
        for y in range(1,s2):
           # print(x,y)
            dp[x][y]=min(dp[x][y-1],dp[x-1][y-1]+abs(arr1[x]-arr2[y]))
            if x==s1-1:
                ans=min(ans,dp[x][y])
    #print(dp)
    if ans==inf:
        ans=0
    print(ans)  



for _ in range(1):
    solve()