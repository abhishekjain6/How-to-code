"""
GIven an array of n integers, with A[i] telling you hwo far you 
can go from the ith index, write a program to find out if you can 
reach the last element or not.
O(n) time
O(1) space
Input:
t, test cases
next t line:
    n integers
Output:
yes/no
"""

for _ in range(int(input())):
    arr=list(map(int,input().split()))
    x=len(arr)-1
    y=x-1
    while(x!=-1 and y!=-1):
        p=arr[x]
        c=1
        while(y>-1):
            if arr[y]<c:
                c+=1
                y-=1
            else:
                x=y
                y=x-1
                break
    #print(x,y)
    if x==0:
        print("Yes")
    else:
        print("No")