"""
https://csacademy.com/contest/fii-code-2021-round-3/task/alex-chills/
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
lcm = lambda a,b : (a*b)//gcd(a,b) 


def lxor(arr):
    ans=0
    for x in arr:
        ans^=x
    return(ans)
def solve():
    n,l,r=mi()
    arr=li()
    arr.append(lxor(arr))
    if r-l>n:
        print(max(arr))
    else:
        p=r-l
        l=l%(n+1)-1
        temp=[]
        for x in range(l,l+p+1):
            temp.append(arr[x%(n+1)])
        print(max(temp))
        #print(temp)

for _ in range(1):
    solve()
