"""
Sort an array around a given pivot element. Formally, givven array a, and pivot a[i], 
all emlements less than a[i] shoulld come before a[i] and elements greater than a[i]
should come after a[i]. You cant use more memory than the given array. 0 based indexing
is used, so 0<=i<n. An O(n) approach is expected, but O(n^2) will work as well.
"""

arr=list(map(int,input().split()))
i=int(input())
idx=0
p=arr[i]
for x in range(len(arr)):
    if arr[x]<p:
        arr[x],arr[idx]=arr[idx],arr[x]
        idx+=1
idx=len(arr)-1
x=0
while (x<idx):

    if arr[x]>p:
        arr[x],arr[idx]=arr[idx],arr[x]
        idx-=1
    x+=1
print(arr)