"""
https://vjudge.net/contest/432331#problem/H
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



MOD=2**33
def solve(n):
    a=ii()
    ans=(pow(2,a,MOD)-1)%MOD
    print("Case {}: {}".format(n+1,ans))
for _ in range(ii()):
    solve(_)