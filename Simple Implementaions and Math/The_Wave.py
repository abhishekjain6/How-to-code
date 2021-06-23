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

def lower(arr,k):
    l,r=0,len(arr)-1
    while(l<r):
        m=l+(r-l)//2
        if k<=arr[m]:
            r=m
        else:
            l=m+1
    if l<len(arr) and arr[l]<k:
        l+=1
    return(l)


def solve():
    n,q=mi()
    arr=li()
    arr.sort()
    qr=[]
    for x in range(q):
        qr.append(ii())
    ans=[]
    d={}
    for x in arr:
        d[x]=1
    if n%2==0:
        ans=[1]
        c=-1
        for x in range(1,n):
            ans.append(c)
            c*=-1
        ans.append(1)
    else:
        ans=[-1]
        c=1
        for x in range(1,n):
            ans.append(c)
            c*=-1
        ans.append(1)
    for q in qr:
        #print(lower(arr,q))
        if q in d:
            print("0")
        
        elif ans[lower(arr,q)]==1:
            print("POSITIVE")
        else:
            print("NEGATIVE")
for _ in range(1):
    solve()