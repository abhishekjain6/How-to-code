from sys import stdin
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


def isdbp(n):
    facts=0
    facts=0
    for x in range(2,n):
        print(n)
        while n%x==0:
            n/=x
            facts+=1
        if facts>=2:
            break
        if n>1:
            facts+=1
        print(facts)
        return(facts==2)


    if facts==2:
        return(True)
    else:
        return(False)
print(isdbp(10),
isdbp(35))

# def solve():
#     n=ii()
#     #print(isdbp(10))
#     for x in range(1,n//2+1):
#              assert(x+n-x==n)
#              if isdbp(x) and isdbp(n-x):
#                  print(x,n-x)
#                  print("YES")
#                  return
#     print("NO")
for _ in range(ii()):
    solve()