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
    n,X=mi()
    w=li()
    s=sum(w)
    w.sort()
    if s==X:
        print("NO")
        return
    else:
        print("YES")
        c=1
        while(c):
            c=0
            rem=[]
            for x in range(1,n):
                rem.append(w[x])
            rem.append(w[0])
            pre=0
            for x in range(n):
                w[x]=rem[x]
                pre+=rem[x]
                if pre==X:
                    c=1
            if c==0:
                print(*w)
                break    


        
for _ in range(ii()):
    solve()