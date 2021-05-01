"""
https://atcoder.jp/contests/zone2021/tasks/zone2021_d
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
    txt=[x for x in input().strip()]
    rev=False
    p=dq()

    for x in txt:
        if x=="R":
            rev=not rev
        elif rev:
            if len(p)>0 and p[0]==x:
                p.popleft()
            else:
                p.appendleft(x)
        else:
            if len(p)>0 and p[-1]==x:
                p.pop()
            else:
                p.append(x)
    if rev:
        p.reverse()
        print("".join(p))
    else:
        print("".join(p))


    
for _ in range(1):
    solve()