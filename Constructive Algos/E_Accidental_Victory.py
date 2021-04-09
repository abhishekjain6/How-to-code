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
    p=[]
    for a,b in enumerate(arr):
        p.append((b,a))
    p.sort(reverse=True)
    #print(p)
    ans=[]
    s=sum(arr)
    for x in range(n):
        if x==n-1:
            if s==p[x][0]:
                ans.append(p[x][1]+1)
        else:
            s-=p[x][0]
            if s<p[x][0]:
                ans.append(p[x][1]+1)
                break
            else:
                ans.append(p[x][1]+1)
    ans.sort()                                                      
    print(len(ans))
    print(*ans)
for _ in range(ii()):
    solve()