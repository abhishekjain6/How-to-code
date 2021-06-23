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




def solve():
    n,q=mi()
    arr=[x for x in input()]
    qr=[]
    for x in range(q):
        a,b=mi()
        qr.append([a,b])
    sqarr=[]
    p=int(sqrt(n))
    for x in range(0,n,p):
        ans=0
        for y in range(x,min(n,x+p)):
            ans+=ord(arr[y])-ord("a")+1
        sqarr.append(ans)
    for y in qr:
        l,r=y[0]-1,y[1]-1
        lb=l//p
        rb=r//p
        ans=0
        if lb==rb:
            for x in range(l,r+1):
                ans+=ord(arr[x])-ord("a")+1
        else:
            for x in range(l,(lb+1)*p):
                ans+=ord(arr[x])-ord("a")+1
            for x in range(lb+1,rb):
                ans+=sqarr[x]
            for x in range(rb*p,r+1):
                ans+=ord(arr[x])-ord("a")+1
        print(ans)
for _ in range(1):
    solve()