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
    mat=[[0 for x in range(n)]for y in range(n)]
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    else:
        a,b=1,2
        for x in range(1,n+1):
            for y in range(1,n+1):
                if a<=n**2:
                    print(a,end=" ")
                    a+=2
                else:
                    print(b,end=" ")
                    b+=2
            print()

for _ in range(ii()):
    solve()