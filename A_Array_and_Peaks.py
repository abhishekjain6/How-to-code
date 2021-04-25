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




def solve():
    n,k=mi()
    if k==0:
        print(*[x for x in range(1,n+1)])
        return
    elif n%2==0:
        if k>n//2-1:
            print(-1)
            return
    elif n%2!=0:
        if k>n//2:
            print(-1)
            return
    if n<3:
        print(-1)
        return
    a=dq([x for x in range(1,n+1)])
    ans=[]
    cp=0
    for x in range(1,n+1):
        if x%2==0 and k>0:
            ans.append(a.pop())
            k-=1
        else:
            ans.append(a.popleft())
    print(*ans)

for _ in range(ii()):
    solve()