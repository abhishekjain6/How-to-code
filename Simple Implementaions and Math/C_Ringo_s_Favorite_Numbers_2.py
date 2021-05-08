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
    tot=0
    for x in arr:
        p=x%200
        q=x//200
        if p==0:
            tot+=1
        else:
            try:
                d[p]+=1
            except:
                d[p]=1
    
    #print(d)
    ans=(tot*(tot-1))//2
    for x in d.keys():
            ans+=(d[x]*(d[x]-1))//2
    print(ans)
for _ in range(1):
    solve()