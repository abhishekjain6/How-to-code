"""
https://vjudge.net/contest/440115#problem/D
"""
from sys import stdin,stdout
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as cmb,permutations as pmb
from math import factorial as f ,ceil,gcd,sqrt,log,inf
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 
from sys import setrecursionlimit as srl
srl(10**4)
a=dd(list)
vis=[False for x in range(200005)]
dis=[0 for x in range(200005)]



def dfs(n):
    vis[n]=True
    for x in a[n]:
        if not vis[x]:
            dis[x]+=dis[n]+1
            dfs(x)      


def solve():
    n=ii()
    for i in range(n-1):
        x,y=mi()
        a[x].append(y)
        a[y].append(x)
    #print(a)
    m=ii()
    dfs(1)
    for i in range(m):
        x=ii()
        if x==1:
            print("0")
        else:
            print(n-dis[x]-1)
    
for _ in range(ii()):
    solve()