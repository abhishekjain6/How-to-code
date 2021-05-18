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
    k=ii()
    a=ii()
    b=ii()
    ans=0
    if k==1:
        ans=a*(n-1)
    else:

        while(n!=1):
            if n%k==0:
                if ((n-(n//k))*a)<b:
                    ans+=a*(n-n//k)
                else:
                    ans+=b
                n//=k
            else:
                if n>k:
                    ans+=(n%k)*a
                    n-=(n%k)
                else:
                    ans+=(n-1)*a
                    n=1
            #print(ans,n,k)
    print(ans)
for _ in range(1):
    solve()