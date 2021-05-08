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
    arr=[]
    for x in range(9):
            arr.append([int(x) for x in input().strip()])
    idx=0
    for x in range(8):
        arr[x][idx]=arr[x][-1]
        idx+=3
        idx%=8
        
    arr[8][-1]=arr[8][0]
    for x in arr:
        print("".join([str(z) for z in x ]))

for _ in range(ii()):
    solve()