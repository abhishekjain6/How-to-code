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


primes=soe(10**6+10)

def solve():
    l,r=mi()
    lft,rt=-1,-1
    while(l<=r):
        if primes[l] and lft==-1:
            lft=l
        if primes[r] and rt==-1:
            rt=r
        if rt!=-1 and lft!=-1:
            break
        l+=1
        r-=1
    if rt==-1 and lft==-1:
        print(-1)
    elif rt==-1 or lft==-1:
        print(0)
    else:
        print(rt-lft)
        
    
for _ in range(ii()):
    solve()