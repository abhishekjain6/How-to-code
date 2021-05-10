"""
https://codeforces.com/contest/1341/problem/B
"""
from sys import stdin
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




def solve():
    n,k=mi()
    arr=li()
    p=[0]
    c=0
    for x in range(1,n-1):
        if arr[x]>arr[x-1] and arr[x]>arr[x+1]:
            c+=1
        p.append(c)
    p.append(c)
    #print(p)
    s,f=0,k-2
    ans=0
    tot=0
    while f<n:
        #print(p[f]-p[s])
        if p[f]-p[s]>tot:
            tot=p[f]-p[s]
            ans=s+1
        s+=1
        f+=1
    if c==0:
        ans=1
    print(tot+1,ans)
        

    
    
for _ in range(ii()):
    solve()