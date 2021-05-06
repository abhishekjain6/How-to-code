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
    d={x:0 for x in range(n)}
    for y in range(len(arr)):
        try:
            d[arr[y]-y]+=1
        except:
            continue
    #print(d)
    ans=0
    for x in range(n):
        p=arr[x]-x
        try:
            ans+=d[p]-1
        except:
            continue
    print(ans//2)
        
        
for _ in range(ii()):
    solve()