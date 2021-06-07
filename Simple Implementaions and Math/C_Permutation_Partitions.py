"""
https://codeforces.com/problemset/problem/1326/C
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
MOD=998244353
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




def solve():
    n,k=mi()
    arr=li()
    p=sorted(arr)
    d={}
    ans1=0
    for x in range(n-1,n-k-1,-1):
        d[p[x]]=1
        ans1+=p[x]
    cx=0
    found=False
    ans2=1
    for x in range(n):
        if arr[x] in d and not found:
            cx=x
            found=True
            continue
        elif arr[x] in d:
            ans2*=(x-cx)
            ans2%=MOD
            cx=x
    print(ans1,ans2%MOD)
for _ in range(1):
    solve()