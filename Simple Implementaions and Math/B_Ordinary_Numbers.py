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
d={1:0}
p=0
for x in range(1,10):
    d[10**x]=p+9
    p+=9
print(d)

def solve():
    n=ii()
    p=len(str(n))
    #print(p)
    ans=d[(10)**(p-1)]
    k=int("1"*p)
    while int(k)<=n:
        ans+=1
        k+=int("1"*p)
    print(ans)



for _ in range(ii()):
    solve()