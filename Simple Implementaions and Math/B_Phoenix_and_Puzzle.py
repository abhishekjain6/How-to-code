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

ans=[]
a1=2
a2=4
cd1=6
cd2=12
while(a1<=10**9):
    ans.append(a1)
    a1+=cd1
    cd1+=4
while(a2<=10**9):
    ans.append(a2)
    a2+=cd2
    cd2+=8


print(len(ans))
def solve():
    
    n=ii()
    if n in ans:
        print("YES")
    else:
        print("NO")
for _ in range(ii()):
    solve()