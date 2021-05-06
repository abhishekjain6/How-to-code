from sys import stdin,stdout
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
    n,t=mi()
    k=ii()
    l,r,d=1,n,0
    ans=n
    while(l<=r):
        m=int((l+r)/2)
        print("? "+str(l)+" "+str(m))
        stdout.flush()
        #q=input()
        x=ii()
        z=m-l+1-x
        if d+z>=k:
            ans=min(ans,m)
            r=m-1
        else:
            l=m+1
            d+=z
    print("! "+str(ans))
    stdout.flush()
for _ in range(1):  
    solve()