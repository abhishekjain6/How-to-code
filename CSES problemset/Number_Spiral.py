"""
https://cses.fi/problemset/task/1071/
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
    x,y=mi()
    done=(max(x,y)-1)*(max(x,y)-1)
    if y>=x:
        if y%2==0:
            ans=done+x
        else:
            ans=done+2*y-x
    else:
        if x%2!=0:
            ans=done+y
        else:
            ans=done+2*x-y
    print(ans)




for _ in range(ii()):
    solve()