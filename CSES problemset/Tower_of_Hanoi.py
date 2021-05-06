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

ans=[]
def toh(n,a,b,c):
    
    if n==1:
        ans.append([a,b])
        return
    toh(n-1,a,c,b)
    ans.append([a,b])
    toh(n-1,c,b,a)

def solve():
    n=ii()
    toh(n,1,3,2)
    print(len(ans))
    for x in ans:
        print(x[0],x[1])
for _ in range(1):
    solve()