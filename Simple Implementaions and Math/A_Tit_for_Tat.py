"""
https://codeforces.com/problemset/problem/1516/A
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
    n,k=mi()
    arr=li()
    a,b=0,n-1
    while k and a<b:
        if arr[a]==0:
            a+=1
            while(arr[a]==0):
                a+=1
                if a>=n-1:
                    break
        if a>=b:
            break
        arr[a]-=1
        arr[b]+=1
        
        k-=1
    print(*arr)
for _ in range(ii()):
    solve()