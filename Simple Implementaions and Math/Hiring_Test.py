"""
https://www.codechef.com/START3B/problems/HIRETEST
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
    n,m=mi()
    x,y=mi()
    ans=[]
    for l in range(n):
        p=[_ for _ in input().strip()]
        #print(p)
        ac=p.count("F")
        par=p.count("P")
        #print(ac,par)
        if ac>=x:
            ans.append("1")
        elif (ac==x-1 and par>=y):
                ans.append("1")
        else:
            ans.append("0")
        #print(ans)
    print("".join(ans)) 
for _ in range(ii()):
    solve()