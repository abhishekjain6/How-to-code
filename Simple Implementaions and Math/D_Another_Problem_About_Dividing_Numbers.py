from sys import stdin,stdout
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter 
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

pos=[1 for x in range(10**5)]
v=[]
def ctr(c):
    tmp=0
    for x in v:
        while(c%x==0):
            c//=x
            tmp+=1
    tmp+=c!=1
    #print(tmp,end=" ")
    return(tmp)




def solve():
    a,b,k=mi()
    if a==b and k==1:
        print("NO")
        return
    if a!=b and k==0:
        print("YES")
        return
    c=gcd(a,b)
    a1=a//c
    a2=b//c
    mn=0
    mx=0
    if a1!=1:
        mn+=1
    if a2!=1:
        mn+=1
    mx=ctr(a)+ctr(b)
    if mn<=k<=mx:
        print("YES")
    else:
        print("NO")




pos=[1 for x in range(10**5)]
pos[0]=0
pos[1]=0
for x in range(2,10**5):
    if pos[x]==1:
        v.append(x)
        for y in range(2*x,10**5,x):
            pos[y]=0
for _ in range(ii()):
    
    solve()