"""
https://codeforces.com/contest/844/problem/B
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
    for x in range(n):
        arr.append(li())
    ans=n*m
    for x in arr:
        w=x.count(1)
        b=x.count(0)
        ans+=2**w-1+2**b-1-w-b
    #print(ans)
    for x in range(m):
        temp=[]
        for y in range(n):
            temp.append(arr[y][x])
        #print(temp)
        w=temp.count(1)
        b=temp.count(0)
        ans+=2**w-1+2**b-1-w-b    
    print(ans)

for _ in range(1):
    solve()