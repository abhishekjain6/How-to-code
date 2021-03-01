"""
Given a set of numbers, find out how many subsets of this set has sum more than or equal to a given number k.
"""
def solve(arr,num):
    m=1<<len(arr)
    ans=0
    for x in range(m):
        csum=0
        for y in range(len(arr)):
            if x&(1<<y):
                csum+=arr[y]
        if csum>=num:
            ans+=1
    print(ans)
numbers=[10,4,5,2,11]
k=11
solve(numbers,k)