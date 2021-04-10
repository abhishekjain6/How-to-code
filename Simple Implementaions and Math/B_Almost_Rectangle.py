"""
https://codeforces.com/contest/1512/problem/B

"""


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
    n=ii()
    arr=[]
    for x in range(n):
        arr.append([x for x in input().strip()])
    idx1=-1
    idx2=-1
    for x in range(n):
        for y in range(n):
            if arr[x][y]=="*":
                if idx1==-1:
                    idx1=[x,y]
                else:
                    idx2=[x,y]
                    break
    idx3=0
    idx4=0
    if idx1[0]==idx2[0]:
        if idx1[0]!=n-1:
            idx3=[idx1[0]+1,idx1[1]]
            idx4=[idx1[0]+1,idx2[1]]
        else:
            idx3=[idx1[0]-1,idx1[1]]
            idx4=[idx1[0]-1,idx2[1]]
    elif idx1[1]==idx2[1]:
        if idx1[1]==n-1:
            idx3=[idx1[0],idx1[1]-1]
            idx4=[idx2[0],idx2[1]-1]
        else:
            
            idx3=[idx1[0],idx1[1]-1]
            idx4=[idx2[0],idx2[1]-1]
    else:
        idx3=[idx1[0],idx2[1]]
        idx4=[idx2[0],idx1[1]]
    #print(idx3,idx4)
    arr[idx3[0]][idx3[1]]="*"
    arr[idx4[0]][idx4[1]]="*"
    for x in range(len(arr)):
        print("".join(arr[x]))
    
for _ in range(ii()):
    solve()