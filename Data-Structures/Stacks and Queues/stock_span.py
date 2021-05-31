"""
https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
"""

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
    arr=li()
    stack=[0]
    ans=[0]*n
    for x in range(n):
        while(len(stack)) and arr[stack[-1]]<=arr[x]:
            stack.pop()
        if not len(stack):
            ans[x]=x+1
        else:
            ans[x]=x-stack[-1]
        stack.append(x)
    print(*ans)
for _ in range(1):
    solve()