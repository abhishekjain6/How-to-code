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
lcm = lambda a,b : (a*b)



def solve():
     n,m,k=mi()
     people=li()
     apt=li()
     people.sort()
     apt.sort()
     i,j=0,0
     ans=0
     while i<n and j<m:
          if people[i]+k<apt[j]:
               i+=1
          elif people[i]-k>apt[j]:
               j+=1
          else:
               i+=1
               j+=1
               ans+=1
     print(ans)




for x in range(1):
         solve()