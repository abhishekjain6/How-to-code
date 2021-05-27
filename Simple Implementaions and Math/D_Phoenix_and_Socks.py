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
    n,l,r=mi()
    arr=li()
    lf={}
    rt={}
    ans=0
    for x in range(l):
        try:
            lf[arr[x]]+=1
        except:
            lf[arr[x]]=1
    for y in range(l,l+r):
        try:
            rt[arr[y]]+=1
        except:
            rt[arr[y]]=1
    for j in list(lf.keys()):
        if j in rt:
            m=min(lf[j],rt[j])
            lf[j]-=m
            rt[j]-=m
            if lf[j]==0:
                del lf[j]
            if rt[j]==0:
                del rt[j]
    lf1=[]
    rt1=[]
    for x in list(lf.keys()):
        for t in range(lf[x]):
            lf1.append(x)
    for y in list(rt.keys()):
        for t in range(rt[y]):
            rt1.append(y)
    #print(lf1,rt1)
    o,p=len(lf1),len(rt1)
    if o>p or p>o:
        if o>p:
            sel=lf1
            rem=p
        else:
            sel=rt1
            rem=o
        d={}
        for x in sel:
            try:
                d[x]+=1
            except:
                d[x]=1
        np=0
        l=0
        for j in list(d.keys()):
                np+=d[j]//2
                l+=d[j]%2
        if rem>l:
            rem-=l
            ans+=l
            np-=rem//2
            ans+=rem
        elif rem<l:
            l-=rem
            ans+=rem
            ans+=l
        else:
            ans+=rem
        
        #print(rem,l,ans,end=" ")
        ans+=np
        
    if o==p:
        ans+=o
    print(ans)
    
for _ in range(ii()):
    solve()