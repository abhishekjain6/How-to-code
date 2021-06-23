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
def ncr(n,r):
    p,k=1,1
    if (n - r < r):
        r = n - r
    if r!=0:
        while(r):
            p,k=p*n,k*r
            m=gcd(p,k)
            p,k=p//m,k//m
            n,r=n-1,r-1
    else:
            p=1
    return(p)



def solve():
    n=ii()
    s=input()
    d={}
    for x in range(n):
        d[s[x]]=1
        if x<=n-1:
            d[s[x:x+2]]=1
        if x<=n-2:
            d[s[x:x+3]]=1
    #print(d["ac"])
    a=ord("a")
    for x in range(26):
        if chr(x+a) not in d:
            print(chr(x+a))
            return
    for x in range(26):
        for y in range(26):
            if chr(x+a)+chr(y+a) not in d:
                print(chr(x+a)+chr(y+a))
                return
    
    for x in range(26):
        for y in range(26):
            for z in range(26):
                if chr(x+a)+chr(y+a)+chr(z+a) not in d:
                    print(chr(x+a)+chr(y+a)+chr(z+a))
                    return
        

    
for _ in range(ii()):
    solve()


    