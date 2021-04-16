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
    arr=[0]
    for x in li():
        arr.append(x)
    pos=[x for x in range(0,n+1)]

    for p in range(ii()):
        #print(arr)
        dist=0
        x,k=mi()
        i=pos[x]
        #print(i)
        dist=0
        v=i-x
        #print(str(pos[x])+"a")
        while(i<=n):
            if arr[i]>=k:
                arr[i]-=k
                dist+=k*v
                break
            else:
                k-=arr[i]
                dist+=arr[i]*v
                v+=1
                arr[i]=0
            i+=1
        if i>n+1:
            i=n+1
        if (i!=n+1 and arr[i]==0):
                i+=1
        x=pos[x]
        while(x<=n and arr[x]==0):
            pos[x]=i
            x+=1
        #print(pos)
        print(dist)
    

for _ in range(1):
    solve()

"""
int n = sc.nextInt();
         int a[] = new int[n+1];
         for(int i=1;i<=n;i++) a[i] = sc.nextInt();
         int q = sc.nextInt();
         int nxt[] = new int[n+1];
         for(int i=1;i<=n;i++) nxt[i] = i;
         while(q-->0) {
          int x = sc.nextInt();
          long k = sc.nextInt();
          int i = nxt[x];
          long ans = 0, v = i-x;
          for(;i<=n;i++) {
           if(a[i]>=k) {
            a[i] -= k;
            ans = ans + k*v;
            break;
           }
           else {
            k -= a[i];
            ans = ans + a[i]*v;
            v++;
            a[i] = 0;
           }
          }
          if(i!=n+1 && a[i]==0) i++;
          x = nxt[x];
          while(x<=n&&a[x]==0) {
           nxt[x++] = i;
          }
          out.write(ans+"\n");
"""