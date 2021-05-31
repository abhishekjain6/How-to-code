"""
https://www.hackerrank.com/challenges/largest-rectangle/copy-from/215879516
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
lcm = lambda a,b : (a*b)
def solve():
    n=ii()
    arr=li()
    arr.append(0)
    stack=[]
    ans=0
    for x in range(len(arr)):
        b=x
        while len(stack) and arr[x]<=stack[-1][0]:
            a,b=stack.pop()
            ans=max(ans,(x-b)*a)
        stack.append([arr[x],b])
    print(ans)



for x in range(1):
    solve()
