"""

https://codeforces.com/problemset/problem/1499/A

"""
for _ in range(int(input())):
    n,k1,k2=map(int,input().split())
    w,b=list(map(int,input().split()))
    maxw=k1//2+k2//2
    if k1%2==1 and k2%2==1:
        maxw+=1
    k1=n-k1
    k2=n-k2
    maxb=k1//2+k2//2
    if k1%2==1 and k2%2==1:
        maxb+=1
    if w<=maxw and b<=maxb:
        print("YES")
    else:
        print("NO")