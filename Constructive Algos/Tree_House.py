from sys import stdin
from sys import setrecursionlimit as srl
input = stdin.readline
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as c,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 
srl(10**4)

MOD=10**9+7
def dfs(arr,node,cnt):
    temp=1
    new=[]
    for x in arr[node]:
        if x!=cnt:
            new.append(dfs(arr,x,node))
    try:
        new.sort(reverse=True)
    except:
        pass
    for x in range(len(new)):
        temp+=new[x]*(x+1)
    return(temp)
def solve():
    N,k=mi()
    arr=[[] for x in range(N+1)]
    for y in range(N-1):
        u,v=mi()
        arr[u].append(v)
        arr[v].append(u)
    #   print(arr)

    print((dfs(arr,1,0)%MOD*k)%MOD)
for _ in range(ii()):
    solve()