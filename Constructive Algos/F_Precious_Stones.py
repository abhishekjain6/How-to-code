"""
https://vjudge.net/contest/432327#problem/F
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




def solve(n):
    s=input().strip()
    arr=[]
    x=0
    sm=1
    while(x<len(s)):
        y=x+1
        while(y<len(s)):
            if s[y]==s[x]:
                 sm+=1
                 y+=1
            else:
                 break
        arr.append(sm)
        sm=1
        x=y
    #print(arr)
    if len(arr)!=1 and s[0]==s[-1]:
        arr[0]+=arr.pop()
    if len(arr)==1:
        if arr[0]==1:
            ans=1
        else:
            ans=arr[0]-1
    else:
        arr.sort()
        #print(arr)
        if arr[-1]==1:
            if len(arr)==2:
                ans=2
            else:
                ans=3
        elif arr[-1]==2:
            if 1 in arr:
                ans=2
            else:
                ans=3
        else:
            if arr[-1]//2>arr[-2]:
                ans=arr[-1]//2
            else:
                ans=arr[-2]
    print("Case {}: {}".format(n+1,ans))
for _ in range(ii()):
    solve(_)