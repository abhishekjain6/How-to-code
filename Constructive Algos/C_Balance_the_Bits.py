from sys import stdin
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as c,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().strip()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b)


for _ in range(ii()):
    n=ii()
    s=input()
    o=s.count("1")
    if s[0]=="0" or s[-1]=="0" or s.count("0")%2!=0 or o%2!=0:
        print("NO")
    else:
        a=""
        b=""
        open=1
        p=o//2
        for x in s:
            if x=="1":
                if p>0:
                    a+="("
                    b+="("
                    p-=1
                else:
                    a+=")"
                    b+=")"
                
            else:
                if open:
                    a+=")"
                    b+="("
                else:
                    a+="("
                    b+=")"
                open=0 if open else 1
        print("Yes")
        print(a)
        print(b)