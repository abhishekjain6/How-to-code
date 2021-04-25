"""
Putting all even entries in an array before the odd ones in constant memory.

"""



arr=list(map(int,input().split()))
idx=0
idx2=len(arr)-1
while(idx<idx2):
    if arr[idx]%2==0:
        idx+=1
    else:
        arr[idx],arr[idx2]=arr[idx2],arr[idx]
        idx2-=1
print(arr)