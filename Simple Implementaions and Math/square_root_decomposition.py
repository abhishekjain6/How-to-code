"""
Given an array of n elements. We need to answer q queries telling the sum of elements in range l to 
r in the array. Also the array is not static i.e the values are changed via some point update query.

Range Sum Queries are of form : Q l r , 
where l is the starting index r is the ending 
index

Point update Query is of form : U idx val, 
where idx is the index to update val is the 
updated value


Should be done in q*sqrt(n) time.

Input:
line 1-N- number of elements of an array
line 2-N space separated values
line 3-Q- number of queries
next q lines:
    query of type 1/2
"""

from math import sqrt


n=int(input())
arr=list(map(int,input().split()))
q=int(input())
qr=[]
for x in range(q):
    a,b=map(int,input().split())
    qr.append([a,b])
sqarr=[]
p=int(sqrt(n))
for x in range(0,n,p):
    sqarr.append(sum(arr[x:x+p]))
for y in qr:
    l,r=y[0],y[1]
    lb,rb=l//p,r//p
    ans=0
    if lb==rb:
        for x in range(l,r+1):
        ans+=arr[x]
    else:
        



