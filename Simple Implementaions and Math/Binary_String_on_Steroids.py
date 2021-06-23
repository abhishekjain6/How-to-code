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
    n=ii()
    arr=[int(x) for x in input()]
    o=arr.count(1)
    z=arr.count(0)
    facs=[]
    for x in range(1,int(sqrt(n))+1):
        if n%x==0:
            if n//x==x:
                facs.append(x)
            else:
                facs.append(n//x)
                facs.append(x)
    #print(facs)
    ans=inf
    for x in facs:
        f=[0 for y in range(x)]
        for i in range(x):
            for j in range(i,n,x):
                if arr[j]==1:
                    f[i]+=1
        r=n//x
        for i in range(x):
            t1=r-2*f[i]+o
            ans=min(ans,t1)
    print(ans)

for _ in range(ii()):
    solve()