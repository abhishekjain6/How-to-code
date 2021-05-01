"""
https://cses.fi/problemset/task/1070
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
    even=[]
    odd=[]
    for x in range(1,n+1):
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
    for x in odd:
        even.append(x)
    for x in range(n-1):
        if abs(even[x]-even[x+1])==1:
            print("NO SOLUTION")
            return
    print(*even)
for _ in range(1):
    solve()