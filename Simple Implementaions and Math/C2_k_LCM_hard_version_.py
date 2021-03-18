"""
https://codeforces.com/contest/1497/problem/C2
"""

for _ in range(int(input())):
    n,k=map(int,input().split())
    for x in range(k-3):
        n-=1
        print("1",end=" ")
    if n%4==0:
        print(str(n//4)+" "+str(n//4)+" "+ str(n//2))
    elif n%4==2:
        print(" ".join(["2",str((n-2)//2),str((n-2)//2)]))
    else:
        print(" ".join(["1",str((n-1)//2),str((n-1)//2)]))