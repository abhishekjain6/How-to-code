"""
Given an array of n elements, find the next greatest permutaion of those 
n elements, in O(n) time and O(1) space.
"""

n=int(input())
arr=list(map(int,input().split()))
modded=arr[:]
k=-1
for x in range(n-1,0,-1):
    if arr[x-1]<arr[x]:
        p=arr[x-1]
        k=x
        break
if k==-1:
    print(0)
    exit()
for x in range(n-1,k-1,-1):
    if arr[x]>p:
        arr[x],arr[k-1]=arr[k-1],arr[x]
        break
y=k
for x in range(n-1,(n-(n-k)//2),-1):
    arr[x],arr[y]=arr[y],arr[x]
    y+=1
print(arr)
