"""

https://www.hackerrank.com/challenges/absolute-permutation/problem

"""



for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[[x,0] for x in range(n+1)]
    flag=1
    for x in range(1,n-k+1):
        if arr[x][1]==0 and arr[x+k][1]==0:
            arr[x][0]=x+k
            arr[x+k][0]=x
            arr[x+k][1]=1
            arr[x][1]=1
        elif arr[x][1]==1 and arr[x+k][1]==0:
            continue
    s=0
    for y in range(1,n+1):
        s+=arr[y][1]
    #print(s)
    if s==n:
        for y in range(1,n+1):
            print(arr[y][0],end=" ")
        print("")
    else:
        print(-1)