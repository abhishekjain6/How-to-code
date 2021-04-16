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
    a=[x for x in input().strip()]
    ans=True
    cnt=0
    for x in a:
        if x=="T":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            ans=False
    a.reverse()
    tot=0
    for x in a:
        if x=="T":
            tot+=1
        else:
            tot-=1
        if tot<0:
            ans=False
    if tot!=n//3:
        ans=False
    if ans:
        print("YES")
    else:
        print("NO")
for _ in range(ii()):
    solve()