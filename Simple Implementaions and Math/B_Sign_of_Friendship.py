"""
https://atcoder.jp/contests/zone2021/tasks/zone2021_b
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
    n,d,h=mi()
    arr=[[0,0]]
    for x in range(n):
        arr.append([x for x in mi()])
    #print(arr)
    slope=[]
    for l in arr:
        slope.append((h-l[1])/(d-l[0]))
    #print(slope)
    print(h-min(slope)*d)
for _ in range(1):
    solve()