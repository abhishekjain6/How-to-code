"""
https://codeforces.com/contest/1514/problem/B
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
    MOD=10**9+7 
    n,k=mi()
    ans=1
    while(k):
        if k%2==1:
            ans*=n
        n=(n**2)%MOD
        k//=2
        
    print(ans%MOD)
    
for _ in range(ii()):
    solve()

    