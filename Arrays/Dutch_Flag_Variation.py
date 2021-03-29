"""
Given array having m distinct values, sort it such that all simmilar
entries appear together.

"""


arr=list(map(int,input().split()))
m=int(input())
x=0
for _ in range(m):
    p=arr[x]
    y=len(arr)-1
    while(x<y):
        if arr[x]!=p:
            arr[x],arr[y]=arr[y],arr[x]
            y-=1
        else:
            x+=1
print(arr)