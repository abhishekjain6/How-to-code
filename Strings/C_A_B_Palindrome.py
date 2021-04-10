"""

https://codeforces.com/contest/1512/problem/C

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


def isp(s):
    return s == s[::-1]

def solve():
    a,b=mi()
    arr=[x for x in input().strip()]
    n=len(arr)
    a-=arr.count("0")
    b-=arr.count("1")
    
    if a<0 or b<0:
        print("-1")
        return
    else:
        f=True
        for i in range(n//2):
            if arr[i]=="?":
                if arr[n-1-i]=="?":
                    continue
                elif arr[n-i-1]=="1":
                    b-=1
                else:
                    a-=1
                arr[i]=arr[n-i-1]
            else:
                if arr[n-i-1]=="?":
                    #print("a")
                    if arr[i]=="1":
                        
                        b-=1
                    else:
                        a-=1
                    arr[n-i-1]=arr[i]
                elif arr[i]!=arr[n-i-1]:
                    f=False
                    break
           # print(i,n-i-1)
            #print("".join(arr)) 
            if a<0 or b<0:
                f=False
                break
            
        if not f:
            print("-1")
            return
        for i in range(n//2):
            #print("".join(arr))
            if arr[i]=="?":
                if a>1:
                    arr[i],arr[n-i-1]="0","0"
                    a-=2
                elif b>1:
                    arr[i],arr[n-i-1]="1","1"
                    b-=2
                else:
                    f=False
                    break
        if not f:
            print("-1")
            return
        m=(n+1)//2-1
        if arr[m]=="?":
            if a>0:
                arr[m]="0" 
            else:
                arr[m]="1"           

        print("".join(arr))    
    


for _ in range(ii()):
    solve()