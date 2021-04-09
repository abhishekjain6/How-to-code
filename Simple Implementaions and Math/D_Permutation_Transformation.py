"""
https://codeforces.com/problemset/problem/1490/D
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


def ct(arr,l,r,dep,dept):
    if r<l:
        return
    elif l==r:
        dept[l]=dep
        return
    else:
        m=arr.index(max(arr[l:r+1]))
        #print(m)
        dept[m]=dep
        ct(arr,l,m-1,dep+1,dept)
        ct(arr,m+1,r,dep+1,dept)

def solve():
    dept=[-1 for x in range(101)]
    n=ii()
    arr=li()
    arr=[[arr[x],0] for x in range(n)]
    d=0
    ct(arr,0,n-1,d,dept)
    for x in dept:
        if x!=-1:
            print(x,end=" ")
        else:   
            break
    print("")
for _ in range(ii()):
    solve()
