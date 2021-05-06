"""
https://codeforces.com/problemset/problem/1496/B
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
    arr.sort()
    mex=-1
    for x in range(n):
        if arr[x]!=x:
            mex=x
            break
    
    ans=len(list(set(arr)))
    if mex==-1:
        mex=arr[-1]+1
        ans+=k
    elif ceil((mex+max(arr))/2) not in arr and k>0:
        ans+=1
    
    print(ans)
for _ in range(ii()):
    solve()