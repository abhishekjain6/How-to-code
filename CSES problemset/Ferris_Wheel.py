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
lcm = lambda a,b : (a*b)



def solve():
        n,X=mi()
        arr=li()
        arr.sort()
        ans=n
        a,b=0,n-1
        while(a<b):
            if arr[a]+arr[b]<=X:
                ans-=1
                a+=1
                b-=1
            else:
                b-=1
        print(ans)  



for x in range(1):
    solve()