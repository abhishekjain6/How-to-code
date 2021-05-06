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
    a=["0","1"]
    for x in range(n-1):
        b=a[:]
        for x in range(len(b)):
            b.append(a.pop())
        a=b[:]
        #print(a)
        for x in range(len(a)//2):
            a[x]="0"+a[x]
        for y in range(len(a)//2,len(a)):
            a[y]="1"+a[y]
    for x in a:
        print(x)
for _ in range(1):
    solve()