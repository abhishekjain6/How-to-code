"""
https://www.hackerrank.com/challenges/simple-text-editor/problem
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
    q=ii()
    undo=[]
    st=""
    for x in range(q):
        
        try:
            a,b=input().split()
        except:
            st=undo.pop()
            continue
        
        if a=="1":
            undo.append(st[:])
            st+=b
        elif a=="2":
            undo.append(st[:])
            st=st[0:len(st)-int(b)]
        else:
            print(st[int(b)-1])
        #print(st,undo)
        
    
for _ in range(1):
    solve()