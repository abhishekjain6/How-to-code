"""
https://codeforces.com/contest/899/problem/C
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
    if n%4==0:
        ans=0
        for x in range(1,n+1):
            if x%4==1 or x%4==0:
                arr.append(x)
    if n%4==1:
        ans=1
        for x in range(1,n+1):
            if x%4==2 or x%4==1:
                arr.append(x)
    if n%4==2:
        ans=1
        for x in range(1,n+1):
            if x%4==3 or x%4==2:
                arr.append(x)
    if n%4==3:
        ans=0
        for x in range(1,n+1):
            if x%4==0 or x%4==3:
                arr.append(x)
    # if n==1:
    #     ans=1
    #     arr=[1]
    # elif n==2:
    #     ans=1
    #     arr=[1]
    # elif n==3:
    #     ans=0
    #     arr=[1,2]
    # elif n==4:
    #     ans=0
    #     arr=[1,4]
    
    print(ans)
    print(len(arr),end=" ")
    print(*arr)
for _ in range(1):
    solve()