"""
https://codeforces.com/contest/1514/problem/C
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
    arr=[]
    mod=1
    for x in range(1,n):
        if gcd(x,n)==1:
            arr.append(x)
            mod=(mod*x)%n
    
    if mod==1:
        print(len(arr))
        print(*arr)
    else:
        print(len(arr)-1)
        print(*arr[:len(arr)-1])
    print()




for _ in range(1):
    solve()