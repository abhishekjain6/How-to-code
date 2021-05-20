"""
https://codeforces.com/contest/1527/problem/A
"""
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
lcm = lambda a,b : (a*b)//gcd(a,b) 


def hp2(n):
 
    p = int(log(n, 2));
    return int(pow(2, p));

def solve():
    n=ii()
    print(hp2(n)-1)
for _ in range(ii()):
    solve()