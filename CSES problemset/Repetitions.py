"""
https://cses.fi/problemset/task/1069
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
    p=[x for x in input().strip()]
    c=0
    cc=p[0]
    ans=0
    for x in range(len(p)):
        if p[x]==cc:
            c+=1
        else:
            cc=p[x]
            c=1
        ans=max(ans,c)
    print(ans)
for _ in range(1):
    solve()