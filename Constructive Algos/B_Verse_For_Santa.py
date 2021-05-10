"""
https://codeforces.com/contest/1279/problem/B
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
    n,s=mi()
    arr=li()
    p=sum(arr)
    q=0
    for x in range(n):
        q+=arr[x]
        if q>s:
            try:
                print(arr.index(max(arr[:x+1]))+1)
            except:
                print(0)
            return()
    print(0)
    
for _ in range(ii()):
    solve()