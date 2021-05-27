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
    k=ii()
    arr=li()
    pref=[]
    a=0
    for x in arr:
        pref.append(a^x)
        a^=x
    if pref[k-1]==0:
        print("YES")
    else:
        m=pref[k-1]
        cx=0
        cnt=0
        for x in arr:
            cx^=x
            if cx==m:
                cnt+=1
                cx=0

        if cx==0 and cnt>1:
            print("YES")
        else:
            print("NO")

for _ in range(ii()):
    solve()