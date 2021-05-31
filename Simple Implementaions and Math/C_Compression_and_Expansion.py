from sys import stdin,stdout
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as cmb,permutations as pmb
from math import factorial as f ,ceil,gcd,sqrt,log,inf
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 
MOD=10**9+7
def soe(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return(prime)




def solve():
    n=ii()
    ii()
    arr=[[] for x in range(n)]
    arr[0].append(1)
    #print(arr)
    for x in range(1,n):
        p=ii()
        idx=len(arr[x-1])-1
        #print(idx)
        if p!=1:
            while(True):
                if arr[x-1][idx]==p-1:
                    idx-=1
                    break
                idx-=1
        for y in range(0,idx+1):
            arr[x].append(arr[x-1][y])
        arr[x].append(p)
        
    #print(arr)
    for x in range(n):
        print(".".join([str(l) for l in arr[x]]))

for _ in range(ii()):
    solve()