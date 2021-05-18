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
    n,X=mi()
    arr=li()
    d={}
    for x in range(n):
        try:
            d[arr[x]].append(x+1)
        except:
            d[arr[x]]=[x+1]
   # print(d)
    for x in range(n):
        if X-arr[x] in d:
            if x+1!=d[X-arr[x]][-1]:
                print(x+1,d[X-arr[x]][-1])
            else:
                 continue
            #print(arr[x])
            return
    print("IMPOSSIBLE")


for _ in range(1):
    solve()