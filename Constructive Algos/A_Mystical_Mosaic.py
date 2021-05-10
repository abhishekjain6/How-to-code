"""
https://codeforces.com/contest/924/problem/A
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
    arr=[]
    ans="Yes"
    for x in range(n):
        arr.append([x for x in input().strip()])
    for x in range(n):
        for y in range(x+1,n):
            if arr[x]==arr[y]:
                continue
            else:
                for t in range(m):
                    if arr[x][t]==arr[y][t] and arr[x][t]=="#":
                        ans="No"
                        print(ans)
                        return()
    print(ans)

for _ in range(1):
    solve()