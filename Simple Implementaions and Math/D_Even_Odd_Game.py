"""
https://codeforces.com/contest/1472/problem/D
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
    n=ii()
    l=li()
    l.sort()
    f=True
    a,b=0,0
    for x in range(n):
        if f:
            y=l.pop()
            if y%2==0:
                a+=y
        else:
            y=l.pop()
            if y%2!=0:
                b+=y
        f= not f
    #print(a,b)
    if a>b:
        print("Alice")
    elif b>a:
        print("Bob")
    else:
        print("Tie")

for _ in range(ii()):
    solve()