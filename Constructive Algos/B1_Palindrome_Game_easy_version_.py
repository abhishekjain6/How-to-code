"""
https://codeforces.com/contest/1527/problem/B1
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


def isp(s):
    return s == s[::-1]
 

def solve():
    n=ii()
    s=[x for x in input()]
    z=s.count("0")
    #print(z)
    if z!=1 and z%2!=0:
        print("ALICE")
    else:
        print("BOB")
for _ in range(ii()):
    solve()