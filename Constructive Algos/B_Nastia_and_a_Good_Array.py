"""
https://codeforces.com/contest/1521/problem/B
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
MOD=1990475947



def solve():
    n=ii()
    arr=li()
    if n==1:
        print(0)
    else:
        print((n+1)//2)
    
        for x in range(0,n,2):
            if x==n-1:
                continue
            else:
                a,b,c=x+1,x+2,min(arr[x],arr[x+1])
                print(a,b,MOD,c)
            arr[x+1]=min(arr[x],arr[x+1])
            #print(arr)
        if len(arr)%2==1:
            print(len(arr)-1,len(arr),min(arr[-1],arr[-2]),MOD)

for _ in range(ii()):
    solve()