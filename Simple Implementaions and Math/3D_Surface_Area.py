"""
https://www.hackerrank.com/challenges/3d-surface-area/problem

"""

x,y=map(int,input().split())
arr=[]
for _ in range(x):
    arr.append(list(map(int,input().split())))
sa=2*x*y
for i in range(len(arr)):
    for j in range(len(arr[i])-1):
            sa+=abs(arr[i][j]-arr[i][j+1])
    sa+=arr[i][0]+arr[i][-1]
d=0
for i in range(len(arr[0])):
    for j in range(len(arr)-1):
        sa+=abs(arr[j][i]-arr[j+1][i])
sa+=sum(arr[0])+sum(arr[-1])
print(sa)
