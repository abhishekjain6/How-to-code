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
    a1,a2,a3=[],[],[]
    for x in range(0,n,2):
        a,b=arr[x],arr[x+1]
        for _ in range(2):
            a1.append(1)
            a2.append(x+1)
            a3.append(x+2)
            a1.append(2)
            a2.append(x+1)
            a3.append(x+2)
            a1.append(2)
            a2.append(x+1)
            a3.append(x+2)
    print(len(a1))
    for x in range( len(a1)):
        print(a1[x],a2[x],a3[x])

        

for _ in range(ii()):
    solve()