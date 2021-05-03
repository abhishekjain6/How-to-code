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



def isp(s):
    return s == s[::-1]
 
def solve():
    arr=[x for x in input().strip()]
    if isp("".join(arr)):
        print("".join(arr))
        return
    mp={}
    for x in arr:
        try:
            mp[x]+=1
        except:
            mp[x]=1
    odd=0
    for x in mp.keys():
        if mp[x]%2!=0:
            odd+=1
        if odd>1:
            print("NO SOLUTION")
            return
    ans=[]
    l=0
    for x in mp.keys():
        if mp[x]%2!=0:
            element_odd=x
            l=mp[x]
        else:
            for y in range(mp[x]//2):
                ans.append(x)
    print("".join(ans),end="")
    for x in range(l):
        print(element_odd,end="")
    print("".join(ans[::-1]))



for _ in range(1):
    solve()