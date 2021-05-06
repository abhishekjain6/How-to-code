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
    arr=[x for x in input().strip()]
    uq=[]
    uq.append(arr[0])
    for x in range(1,n):
        if arr[x]!=arr[x-1]:
            uq.append(arr[x])
    for y in uq:
        if uq.count(y)>1:
            print("NO")
            return
    print("YES")

for _ in range(ii()):
    solve()