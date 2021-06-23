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

import sys

stack=[]

MOD=10**9+7
def soe(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return(prime)
def ncr(n,r):
    p,k=1,1
    if (n - r < r):
        r = n - r
    if r!=0:
        while(r):
            p,k=p*n,k*r
            m=gcd(p,k)
            p,k=p//m,k//m
            n,r=n-1,r-1
    else:
            p=1
    return(p)
d=dd(list)
vis=[]
def dfs(n,d,vis):
    vis[n]=1
    for x in d[n]:
        if not vis[x]:
            dfs(x,d,vis)


def solve():
    n=ii()
    f=[x-1 for x in li()]
    s=[x-1 for x in li()]
    d.clear()
    for x in range(n):
        d[f[x]].append(s[x])
        d[s[x]].append(f[x])
    vis=[0 for x in range(n)]
    ans=0
    for x in range(n):
        if not vis[x]:
            ans+=1
            dfs(x,d,vis)
    print(pow(2,ans,MOD))
    
    


for _ in range(ii()):
    solve()