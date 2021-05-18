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
    d={}
    for x in arr:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    ans=len(d)
   # print(d)
    p=[x for x in d.keys()]
    for x in p:
        if d[x]>1:
            if x+1 not in d:
                ans+=1
                d[x+1]=1
            elif x-1 not in d and x!=1:
                ans+=1
                d[x-1]=1
      #  print(ans)
    #print(d)
    print(ans)
for _ in range(ii()):
    solve()