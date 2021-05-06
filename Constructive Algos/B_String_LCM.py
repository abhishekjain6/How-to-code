"""
https://codeforces.com/contest/1473/problem/B
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
    s=input().strip()
    t=input().strip()
    if lcm(len(s),len(t))//len(s)*s==lcm(len(s),len(t))//len(t)*t:
        print(lcm(len(s),len(t))//len(s)*s)
    else:
        print(-1)
            
for _ in range(ii()):
    solve()