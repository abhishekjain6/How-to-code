"""

https://codeforces.com/contest/1497/problem/C1

"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%4==0:
        print(str(n//4)+" "+str(n//4)+" "+ str(n//2))
    elif n%4==2:
        print(" ".join(["2",str((n-2)//2),str((n-2)//2)]))
    else:
        print(" ".join(["1",str((n-1)//2),str((n-1)//2)]))
