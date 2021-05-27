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


def solve(s1):
    s2=input()
    a=0
    b=0
    while(a<len(s1) and b<len(s2)):
        if s1[a]==s2[b]:
            a+=1
            b+=1
        else:
            a+=1
    if b==len(s2):
        print("POSITIVE")
    else:
        print("NEGATIVE")
    


a=input()
for _ in range(ii()):
    solve(a)