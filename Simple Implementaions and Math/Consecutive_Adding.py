"""
https://www.codechef.com/MARCH21B/problems/CONSADD


Note, this problem can be solved using bipartite graphs as well
"""
for _ in range(int(input())):
    r,c,x=map(int,input().split())
    a=[]
    b=[]
    arr=[[0 for z in range(c)]for y in range(r)]
    for z in range(r):
        a.append(list(map(int,input().split())))
    for y in range(r):
        b.append(list(map(int,input().split())))
    for i in range(r):
        for j in range(c):
            arr[i][j]=b[i][j]-a[i][j]
 
    for j in range(c):
        t1=0
        t2=r-x
        while t2>=0:
            t1+=arr[t2][j]
            t2-=x
        i=r-1
        while i>r-x:
       
            t3=i-x
            while t3>=0:
                arr[i][j]+=arr[t3][j]
                t3-=x
            arr[i][j]-=t1
            i-=1
    i=r-1
    while i>r-x:
        t1=0
        t2=c-x
        while t2>=0:
            t1+=arr[i][t2]
            t2-=x
        j=c-1
        while j>c-x:
            t3=j-x
            while t3>=0:
                arr[i][j]+=arr[i][t3]
                t3-=x
            arr[i][j]-=t1
            j-=1
        i-=1
    flag=0
    for i in range(r-1,r-x,-1):
        for j in range(c-1,c-x,-1):
            if arr[i][j]!=0:
                flag=1
                break
    if not flag:
        print("Yes")
    else:
        print("No")

