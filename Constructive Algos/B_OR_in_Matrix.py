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
    arr=[]
    for x in range(n):
        arr.append(li())
    p=[[1 for x in range(m)]for x in range(n)]
    #print(p[0][0])
    for x in range(n):
        for y in range(m):
            if arr[x][y]==0:
                p[x]=[0 for l in range(m)]
                #print(p)
                for z in range(n):
                    #print(z,y)
                    #print(p[0][0])
                    p[z][y]=0
    k=[[0 for x in range(m)]for y in range(n)]
    for x in range(n):
        for y in range(m):
            if p[x][y]==1:
                k[x]=[1 for o in range(m)]
                for z in range(n):
                    k[z][y]=1
    if k==arr:
        print("YES")
        for x in p:
            print(*x)
    else:
        print("NO")
for _ in range(1):
    solve()