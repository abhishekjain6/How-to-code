"""
Given an array of stock prices over the days,
find max profit that can be earned by buying and selling
the stock at max twice.
"""

# Caculate 2 arrays, max profit possible by selling beofre the xth day
# and max profit possible by selling after or on the xth day. Add these
# two, and the max value will be the answer.

arr=list(map(int,input().split()))
cmin=arr[0]
maxp=0
n=len(arr)
profit_till=[0]
for x in range(1,n):
    maxp=max(maxp,arr[x]-cmin)
    cmin=min(cmin,arr[x])
    profit_till.append(maxp)
profit_after=[0]
maxp=0
cmax=arr[n-1]
for x in range(n-2,-1,-1):
    maxp=max(maxp,cmax-arr[x])
    cmax=max(arr[x],cmax)
    profit_after.append(maxp)
maxarr=[]
for x in range(n):
    maxarr.append((profit_till[x]+profit_after[n-x-1]))
print(max(maxarr))
