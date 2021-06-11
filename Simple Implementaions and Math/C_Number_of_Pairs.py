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

def lower(arr,n,x):
    l,r=0,n-1
    while(l<=r):
        m=(l+r)//2
        if (arr[m] >= x):
            r = m - 1;
        else:
            l = m + 1;
    return(l)
def upper(arr,n,x):
    l,r=0,n-1
    while(l<=r):
        m=(l+r)//2
        if (arr[m] <= x):
            l=m+1;
        else:
            r=m-1;
    return(r)
def ctr(arr,n,x,y):
    return(upper(arr,n,y)-lower(arr,n,x)+1)

def solve():
    n,l,r=mi()
    arr=li()
    arr.sort()
    ans=0
    for x in range(n):
        if arr[x]>r:
            continue
        if arr[x]<l:
            cnt=ctr(arr,n,l-arr[x],r-arr[x])
            if (arr[x]<=(r-arr[x])) and (arr[x]>=(l-arr[x])):
                cnt-=1
        else:
                cnt=ctr(arr,n,0,r-arr[x])
                if arr[x]<=(r-arr[x]):
                    cnt-=1
        ans+=cnt
    print(ans//2)

for _ in range(ii()):
    solve()