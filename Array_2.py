"""
Write a program to take input as an array and a key, and update 
the array so that all occurences of the key have been removed and 
the remaining elements have been shifted to fill in the empty indices.
Rerturn number of remaining elements, the vlaues beyond the last valid entry 
can be anything.
"""
arr=list(map(int,input().split()))
k=int(input())
x=arr.index(k)
y=x
n=len(arr)
while y<n:
    
    if arr[y]!=k:
        arr[x]=arr[y]
        x+=1
        y+=1
    else:
        y+=1
print(x)