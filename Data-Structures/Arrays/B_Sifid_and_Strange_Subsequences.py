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
lcm = lambda a,b : (a*b)



def solve():
    n=ii()
    arr=li()
    p=[]
    m=inf
    for x in arr:
        if x<=0:
            p.append(x)
        else:
                m=min(m,x)
    p.sort()
    poss=True
    for x in range(1,len(p)):
        if p[x]-p[x-1]<m:
            poss=False
    if m==inf:
        poss=False
    ans=len(p)
    if poss:
        ans+=1
    if n==1:
        ans=1
    print(ans)
    

for x in range(ii()):
    solve()