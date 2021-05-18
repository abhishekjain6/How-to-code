from sys import stdin,stdout
input = stdin.readline
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as c,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 




def solve():
    arr=[4,8,15,16,23,42]
    d={}
    for x in range(6):
        for y in range(x+1,6):
            d[arr[x]*arr[y]]=[arr[x],arr[y]]
    arr=[0 for x in range(6)]
    n,m=1,2
    idx=1
    idx1=0
    for x in range(2):
        print("?",n,m)
        stdout.flush()
        n1=ii()
        #print(n1)
        a,b=d[n1]
        print("?",n+1,m+1)
        stdout.flush()
        n2=ii()
        c,q=d[n2]
        if a==c:
            arr[idx]=a
            arr[idx1]=n1//a
            arr[idx1+2]=n2//c
        elif a==q:
            arr[idx]=a
            arr[idx1]=n1//a
            arr[idx1+2]=n2//q
        elif b==q:
            arr[idx]=b
            arr[idx1]=n1//b
            arr[idx1+2]=n2//q
        else:
            arr[idx]=b
            arr[idx1]=n1//b
            arr[idx1+2]=n2//c
        idx=4
        idx1=3
        n=4
        m=5
    print("!",*arr)
    stdout.flush()








for _ in range(1):
    solve()