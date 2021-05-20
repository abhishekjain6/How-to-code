"""
https://codeforces.com/contest/1527/problem/C
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




def solve():
    n=ii()
    arr=li()
    d={}
    for x in range(n):
        try:
            d[arr[x]].append(x+1)
        except:
            d[arr[x]]=[x+1]
    #print(d)
    ans=0
    for x in d:
        p=len(d[x])
        temp=[0 for x in range(p)]
        temp[0]=d[x][0]
        for y in range(1,p):
            temp[y]=temp[y-1]+d[x][y]
        print(temp)
        for y in range(p-1,0,-1):
            ans+=(n-d[x][y])*temp[y-1]+1
    print(ans*2)
for _ in range(ii()):
    solve()

     