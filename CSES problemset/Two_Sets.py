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
    if n%4!=3 and n%4!=0:
        print("NO")
    else:
        print("YES")
        if n%4==0:
            a1=[]
            a2=[]
            for x in range(1,n+1):
                if x%4==1 or x%4==0:
                    a1.append(x)
            for x in range(1,n):
                if x%4!=1 and x%4!=0:
                    a2.append(x)
        if n%4==3:
            a1=[1,2]
            a2=[3]
            for x in range(4,n+1):
                if x%4==0 or x%4==3:
                    a1.append(x)
            for x in range(4,n):
                if x%4!=3 and x%4!=0:
                    a2.append(x)
        print(len(a1))
        print(*a1)
        print(len(a2))
        print(*a2)


for _ in range(1):
    solve()