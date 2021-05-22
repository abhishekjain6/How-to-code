"""
https://vjudge.net/contest/440115#problem/J
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




def solve():
    s=dq([x for x in input()])
    k=ii()
    m=dq([x for x in str(bin(k)).lstrip("0b")])
    if len(m)>len(s):
        while(len(s)!=len(m)):
            s.appendleft("0")
    if len(m)<len(s):
        while(len(m)!=len(s)):
            m.appendleft("0")
    #print(s,m)
    ans=[]
    c=0
    for x in range(len(m)-1,-1,-1):
        a,b=int(m[x]),int(s[x])
        sm=a^b^c
        c=(a and b) or (b and c) or (a and c)
        ans.append(str(sm))
    if c==1:
        ans.append("1")
    print("".join(ans[::-1]))
    #print(2*"x")


    print(len(1234))
for _ in range(ii()):
    solve()