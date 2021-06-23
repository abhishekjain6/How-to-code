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
    arr=[]
    ans=0
    for x in range(n):
        a,b=mi()
        ans+=2*a
        arr.append([a,b])
    arr.sort(key=lambda x: x[1])
    arr.reverse()
    l,r=0,n-1
    pos=0
    while(l<=r):
        m=arr[r][1]
        if l==r:
            t1=arr[l][0]
            t2=max(0,arr[l][1]-pos)
            t1=max(0,t1-t2)
            ans-=t1
            break
        elif pos>=m:
            pos+=arr[r][0]
            ans-=arr[r][0]
            r-=1
        elif pos+arr[l][0]<=arr[r][1]:
            pos+=arr[l][0]
            arr[l][0]=0
            l+=1
        else:
            t1=arr[r][1]-pos
            pos+=t1+arr[r][0]
            arr[l][0]-=t1
            ans-=arr[r][0]
            r-=1
    print(ans)

for _ in range(1):
    solve()