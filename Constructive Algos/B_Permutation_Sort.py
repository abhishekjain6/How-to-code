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
    arr=li()
    p=sorted(arr)
    if arr==sorted(arr):
        ans=0
    elif arr[0]==1 or arr[n-1]==n:
        ans=1
    elif arr[0]==n and arr[n-1]==1:
        ans=3
    else:
        ans=2
    
    print(ans)
for _ in range(ii()):
    solve()