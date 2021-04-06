"""
https://www.codechef.com/ICM2021B/problems/ICM0001
"""

from collections import deque
def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    p=sorted(arr)
    fans=[]
    ans=deque([arr[n-1]])
    if arr==p:
        print("YES")
        print("0")
    else:
        l=0
        moves=0
        for x in range(n-2,-1,-1):
            if arr[x]<=arr[x+1]:
                ans.appendleft(arr[x])
            else:
                for z in list(ans):
                    fans.append(z)
                moves+=1
                ans=deque([arr[x]])
            
        for z in list(ans):
            fans.append(z)
        for x in range(1,n):
            if fans[x]<fans[x-1]:
                print("NO")
                return
            else:
                continue
        print("YES")
        print(moves)
for _ in range(int(input())):
    solve()