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
    n,m,X=mi()
    arr=li()
    ans=[0]*n
    h=[]
    for x in range(m):
        h.append([arr[x],x+1])
        ans[x]=x+1
    heapify(h)
    for x in range(m,n):
        y=heappop(h)
        ans[x]=y[-1]
        y[0]+=arr[x]
        heappush(h,y)
    print("YES")
    print(*ans  )
        
for _ in range(ii()):
    solve()