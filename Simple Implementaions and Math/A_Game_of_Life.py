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
    n,m=mi()
    arr=[x for x in input().strip()]
    pz=n-arr.count("1")
    old=arr
    new=arr[:]
    if pz==0 or pz==n:
        print("".join(arr))
        return
    for x in range(1,n-1):
        if arr[x-1]=="1" and arr[x+1]=="1":
            pz-=1
    while(pz!=0 and m!=0):
        for x in range(n):
            if x==0:
                if old[1]=="1":
                    new[0]="1"
                    pz-=1
            elif x==n-1:
                if old[x-1]=="1":
                    new[-1]="1"
                    pz-=1
            else:
                if old[x]=="0" and not(old[x-1]=="1" and old[x+1]=="1"):
                    if (old[x-1]=="1" or old[x+1]=="1"):
                        new[x]="1"
                        pz-=1
        old=new[:]
        print("".join(new)) 
        m-=1
    print("".join(new))            
                
for _ in range(ii()):
    solve()