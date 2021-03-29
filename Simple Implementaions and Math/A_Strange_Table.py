"""
https://codeforces.com/contest/1506/problem/0
"""
for _ in range(int(input())):
    n,m,k=list(map(int,input().split()))
    r=k%n
    if r==0:
        r=n
    
    
    if k%n==0:
        c=k//n
    else:
        c=(k-k%n)//n+1

    c=min(c,m)
    # print(r,c)
    print(m*(r-1)+c)