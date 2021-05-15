"""
https://codeforces.com/contest/1040/problem/B
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
    mx=k*2+1
    rem=n%mx
    ans=[]
    if rem==0:
        for x in range(k+1,n-k+2,2*k+1):
            ans.append(x)
    else:
        if rem>k:
            for x in range(rem-k,n+1,2*k+1):
                ans.append(x)
        else:
            for x in range(rem,n+1,2*k+1):
                ans.append(x)
    if k==0:
        ans=[x for x in range(1,n+1)]
    print(len(ans))
    print(*ans)
for _ in range(1):
    solve()