"""
Given an array of stock prices over the days,
find max profit that can be earned by buying and selling
the stock one time.
"""

arr=list(map(int,input().split()))
cmin=arr[0]
maxp=0
for x in range(1,len(arr)):
    maxp=max(maxp,arr[x]-cmin)
    cmin=min(cmin,arr[x])
print(maxp)
