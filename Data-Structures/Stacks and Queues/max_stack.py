"""
Given N numbers and a push/pop request, return the maximum element in the stack after the current operation.
Input: number n,q
       n space separated integers
       q space separated integers, 1 for push, 0 for pop
q>=n
Output:
       q space separated integers, the max value in the stack after operations    
""" 

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
lcm = lambda a,b : (a*b)//gcd(a,b) 


n,q=mi()
arr=li()
inst=li()
stack=[arr[0]]
m=[arr[0]]
ans=[]
ptr=1
for x in range(1,q):
    #3print(*m)
    if inst[x]==1:
        stack.append(arr[ptr])
        t=arr[ptr]
        ptr+=1
        #print(t)
        m.append(max(m[-1],t))
    elif inst[x]==0:
        t=stack.pop()
        if len(stack)==0:
            m.append(0)
        else:
            if m[-1]==t:
                try:
                    m.append(m[-2])
                except:
                    m.append(0)
            
print(*m)
    
