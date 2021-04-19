""""
https://atcoder.jp/contests/arc117/tasks/arc117_a
""""


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
    a,b=mi()
    if a>b:
        ans=[]
        p,q=0,0
        for x in range(1,a+1):
            ans.append(x)
            p+=x
        for y in range(1,b):
            ans.append(-y)
            q+=y
        ans.append(q-p)
        print(*ans)
    elif b>a:
        ans=[]
        p,q=0,0
        for x in range(1,b+1):
            ans.append(-x)
            p+=x
        for y in range(1,a):
            ans.append(y)
            q+=y
        ans.append(p-q)
        print(*ans)
    else:
        ans=[]
        for x in range(1,a+1):
            ans.append(x)
            ans.append(-x)
        print(*ans)

    
for _ in range(1):
    solve()