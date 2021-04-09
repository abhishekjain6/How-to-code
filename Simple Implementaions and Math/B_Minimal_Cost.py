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
    n,u,v=mi()
    arr=li()
    ans=0
    diff=0
    for x in range(n-1):
        diff=max(diff,abs(arr[x]-arr[x+1]))
    if diff==0:
        ans=v+min(u,v)
    elif diff==1:
        ans=min(u,v)
    else:
        ans=0
    print(ans)
for _ in range(ii()):
    solve()