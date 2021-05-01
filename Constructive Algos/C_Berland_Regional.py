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
    u=li()
    s=li()
    d={}
    for x in range(n):
        try:
            d[u[x]].append(s[x])
        except:
            d[u[x]]=[s[x]]
    ans=[0 for p in range(n)]
    for x in d.keys():
        d[x].sort(reverse=True)
        psum=[]
        csum=0
        for y in range(len(d[x])):
            csum+=d[x][y]
            psum.append(csum)
       
        for k in range(1,len(d[x])+1):
            left=len(d[x])-(len(d[x])%k)
            ans[k-1]+=psum[left-1]
            #print(psum[left-1],ans[k-1],k)
    print(*ans)

for _ in range(ii()):
    solve()