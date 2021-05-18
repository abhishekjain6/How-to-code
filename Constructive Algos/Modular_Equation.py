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
    n,m=mi()
    arr=[1 for x in range(n+1)]
    ans=0
    if n<=10**3 and m<=10**5:
        ans=0
        for x in range(1,n+1):
            for y in range(x+1,n+1):
                if (m%x)%y==(m%y)%x:
                 ans+=1
    else:
        for x in range(2,n+1):
            mod=m%x
            ans+=arr[mod]
            for y in range(mod,n+1,x):
                arr[y]+=1
    print(ans)


for _ in range(ii()):
    solve()