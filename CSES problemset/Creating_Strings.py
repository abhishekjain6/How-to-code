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
    ans=[]
    n=[x for x in input().strip()]
    y=list(p(n,len(n)))
    ans=[]
    uq=[]
    for x in n:
        if x not in uq:
            uq.append(x)
    if n==uq and len(n)==8:
        ans=y[:]
    else:
        for x in y:
            if x not in ans:
                ans.append(x)
        
    print(len(ans))
    for x in range(len(ans)):
        ans[x]="".join(ans[x])
    ans.sort()
    for x in ans:
        print(x)

for _ in range(1):
    solve()