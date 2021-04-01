"""
Given an array of n numbers, find the sequence just lexographically smaller than it.
"""

arr=list(map(int,input().split()))
n=len(arr)
for x in range(1,n):
    if arr[x-1]>arr[x]:
        p=x
for x in range(p,n):
    if arr[x]<arr[p-1]:
        q=x
arr[p-1],arr[q]=arr[q],arr[p-1]
y=n-1
for x in range(p,n-(n-p)//2):
    arr[x],arr[y]=arr[y],arr[x]
    y-=1
print(arr)