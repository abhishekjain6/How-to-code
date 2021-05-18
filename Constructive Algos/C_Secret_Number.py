from sys import stdin
input = stdin.readline
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as cmb,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 


def nCr(n, r):
     
    return (f(n) / (f(r)* f(n - r)))

def nPr(n, r):
     
    return math.floor(fact(n) /
                fact(n - r))
def solve():
    s=[x for x in input().strip()]
    cnf=[]
    pos=[]
    for x in range(10):
        if s[x]=="o":
            for y in range(4):
                cnf.append(x)
        if s[x]=="?":
            pos.append(x)
    #print(cnf,pos)
    print(4*len(pos)*len(set(cmb(cnf,4))))
    
for _ in range(1):
    solve()