"""
Given a set of n numbers, generate a uniformly random set of 
k numbers taken from these n numbers.
"""
from random import randint as rnd

n=int(input())
arr=[x for  x in range(n)]
k=int(input())
for y in range(k):
    p=rnd(y,n-1)
    arr[y],arr[p]=arr[p],arr[y]  #Swap two indexes, out of which one was taken at random.
print(arr)